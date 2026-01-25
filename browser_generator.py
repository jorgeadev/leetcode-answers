import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import os
import re
import pickle
import tempfile
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from html.parser import HTMLParser
try:
    from PIL import Image
    import pytesseract
    import io
    OCR_AVAILABLE = True
except ImportError:
    OCR_AVAILABLE = False
    print("OCR not available. Install with: pip install pillow pytesseract")

temp_dir = os.path.join(tempfile.gettempdir(), 'leetcode_generator')
driver = None

class HTMLToMarkdown(HTMLParser):
    """Convert HTML to Markdown format."""
    def __init__(self):
        super().__init__()
        self.markdown = []
        self.in_pre = False
        self.in_code = False
        self.in_strong = False
        
    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.markdown.append('\n')
        elif tag == 'code':
            self.markdown.append('`')
            self.in_code = True
        elif tag == 'pre':
            self.markdown.append('\n```\n')
            self.in_pre = True
        elif tag == 'strong':
            self.markdown.append('**')
            self.in_strong = True
        elif tag == 'em':
            self.markdown.append('*')
        elif tag == 'li':
            self.markdown.append('\n- ')
        elif tag == 'ul':
            self.markdown.append('\n')
        elif tag == 'sup':
            self.markdown.append('^')
        elif tag == 'img':
            # Extract image source
            src = None
            alt = ''
            for attr_name, attr_value in attrs:
                if attr_name == 'src':
                    src = attr_value
                elif attr_name == 'alt':
                    alt = attr_value
            if src:
                # Handle relative URLs
                if src.startswith('//'):
                    src = 'https:' + src
                elif src.startswith('/'):
                    src = 'https://leetcode.com' + src
                # Add markdown image with full URL
                self.markdown.append(f'\n![{alt}]({src})\n')
            
    def handle_endtag(self, tag):
        if tag == 'p':
            self.markdown.append('\n')
        elif tag == 'code':
            self.markdown.append('`')
            self.in_code = False
        elif tag == 'pre':
            self.markdown.append('\n```\n')
            self.in_pre = False
        elif tag == 'strong':
            self.markdown.append('**')
            self.in_strong = False
        elif tag == 'em':
            self.markdown.append('*')
        elif tag == 'ul':
            self.markdown.append('\n')
            
    def handle_data(self, data):
        self.markdown.append(data)
        
    def get_markdown(self):
        text = ''.join(self.markdown)
        # Clean up multiple newlines
        text = re.sub(r'\n{3,}', '\n\n', text)
        return text.strip()

def html_to_markdown(html_content):
    """Convert HTML to Markdown."""
    parser = HTMLToMarkdown()
    parser.feed(html_content)
    return parser.get_markdown()

def extract_problem_name(url):
    """Extract problem name from LeetCode URL."""
    match = re.search(r'/problems/([^/]+)/', url)
    if match:
        return match.group(1).replace('-', '_')
    return None

def get_existing_folders():
    """Get list of existing folders in python directory."""
    python_dir = "python"
    folders = ["+ Create New Folder"]
    
    if os.path.exists(python_dir):
        try:
            # Get only root level subdirectories in python folder
            for folder in os.listdir(python_dir):
                folder_path = os.path.join(python_dir, folder)
                if os.path.isdir(folder_path):
                    folders.append(folder)
        except Exception as e:
            print(f"Error reading folders: {e}")
    
    return folders

def on_folder_selection_change(event):
    """Show/hide custom folder name input based on selection."""
    if folder_combo.get() == "+ Create New Folder":
        custom_folder_label.pack(anchor="w", pady=(5, 0))
        custom_folder_entry.pack(pady=5, fill="x")
    else:
        custom_folder_label.pack_forget()
        custom_folder_entry.pack_forget()

def open_browser():
    """Open browser with Selenium for login."""
    global driver
    if driver:
        driver.quit()
    options = Options()
    options.add_argument(f"--user-data-dir={temp_dir}")
    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://leetcode.com/accounts/login/")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open browser. Make sure ChromeDriver is installed and in PATH.\nError: {str(e)}")

def close_browser():
    """Close browser and save session."""
    global driver
    if driver:
        try:
            cookies = driver.get_cookies()
            with open(os.path.join(temp_dir, 'cookies.pkl'), 'wb') as f:
                pickle.dump(cookies, f)
        except Exception as e:
            print(f"Error saving cookies: {e}")
        driver.quit()
        driver = None
        messagebox.showinfo("Info", "Browser closed and session saved.")
    else:
        messagebox.showwarning("Warning", "No browser is open.")

def generate_from_url():
    """Generate folder structure from URL - fully automatic."""
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter the LeetCode URL.")
        return

    global driver
    if not driver:
        options = Options()
        options.add_argument(f"--user-data-dir={temp_dir}")
        try:
            driver = webdriver.Chrome(options=options)
            # Load cookies
            try:
                with open(os.path.join(temp_dir, 'cookies.pkl'), 'rb') as f:
                    cookies = pickle.load(f)
                    driver.get("https://leetcode.com")
                    for cookie in cookies:
                        driver.add_cookie(cookie)
            except Exception as e:
                print(f"Error loading cookies: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open browser. Make sure ChromeDriver is installed.\nError: {str(e)}")
            return

    driver.get(url)
    print("Waiting for page to load...")
    time.sleep(8)  # Initial wait for page load

    # Wait for description element to be present
    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".elfjS, [data-track-load='description_content'], .content__u3I1")))
        print("Description element detected")
    except:
        print("Timeout waiting for description element, continuing anyway...")

    difficulty = "medium"  # default
    description = ""
    problem_title = ""
    prefix = ""
    initial_code = ""

    try:
        # Extract problem number and title from the page
        try:
            # Try multiple selectors for title
            title_selectors = ["a.no-underline", "[data-cy='question-title']", ".text-title-large", "a[href*='/problems/']"]
            for selector in title_selectors:
                try:
                    title_element = driver.find_element(By.CSS_SELECTOR, selector)
                    problem_title = title_element.text
                    if problem_title and len(problem_title) > 0:
                        print(f"Found title: {problem_title}")
                        # Extract prefix from title (e.g., "4. Median..." -> "4")
                        prefix_match = re.match(r'^(\d+)\.', problem_title)
                        if prefix_match:
                            prefix = prefix_match.group(1)
                            print(f"Extracted prefix: {prefix}")
                        break
                except:
                    continue
        except Exception as e:
            print(f"Could not find problem title: {e}")

        # Try to find difficulty
        try:
            # Look for difficulty in various places
            difficulty_selectors = [
                "div[diff='Easy']",
                "div[diff='Medium']",
                "div[diff='Hard']",
                "div[class*='text-difficulty-easy']",
                "div[class*='text-difficulty-medium']", 
                "div[class*='text-difficulty-hard']",
                "div.text-easy",
                "div.text-medium",
                "div.text-hard",
                "span.text-easy",
                "span.text-medium",
                "span.text-hard"
            ]

            for selector in difficulty_selectors:
                try:
                    element = driver.find_element(By.CSS_SELECTOR, selector)
                    # Check both text content and diff attribute
                    text = element.text.lower().strip()
                    diff_attr = element.get_attribute('diff')

                    if diff_attr and diff_attr.lower() in ['easy', 'medium', 'hard']:
                        difficulty = diff_attr.lower()
                        print(f"Found difficulty from attribute: {difficulty}")
                        break
                    elif text in ['easy', 'medium', 'hard']:
                        difficulty = text
                        print(f"Found difficulty from text: {difficulty}")
                        break
                except:
                    continue

            # If still not found, search for all divs and spans near the title
            if difficulty == "medium":  # Still default, not detected yet
                try:
                    # Get all small text elements that might contain difficulty
                    elements = driver.find_elements(By.CSS_SELECTOR, "div, span")
                    for elem in elements:
                        text = elem.text.strip().lower()
                        if text == 'easy':
                            difficulty = 'easy'
                            print(f"Found difficulty via text search: easy")
                            break
                        elif text == 'medium':
                            difficulty = 'medium'
                            print(f"Found difficulty via text search: medium")
                            break
                        elif text == 'hard':
                            difficulty = 'hard'
                            print(f"Found difficulty via text search: hard")
                            break
                except:
                    pass

            print(f"Final detected difficulty: {difficulty}")
        except Exception as e:
            print(f"Difficulty detection error: {e}, using default: medium")

        # Get the problem description
        description_selectors = [
            ("css selector", "div.elfjS[data-track-load='description_content']"),
            ("css selector", "div.elfjS"),
            ("css selector", "[data-track-load='description_content']"),
            ("css selector", ".content__u3I1"),
            ("css selector", ".question-content"),
            ("css selector", ".xFUwe"),
            ("css selector", "div._1l1MA")
        ]

        for method, selector in description_selectors:
            try:
                element = driver.find_element(By.CSS_SELECTOR, selector)
                # Scroll to element to ensure it's loaded
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                time.sleep(1)

                # Get innerHTML to preserve formatting
                description_html = element.get_attribute('innerHTML')
                if description_html and len(description_html) > 50:
                    # Convert HTML to Markdown
                    description = html_to_markdown(description_html)
                    print(f"Found description using selector: {selector} ({len(description)} chars)")
                    break
            except Exception as e:
                print(f"Selector {selector} failed: {str(e)[:100]}")
                continue

        # If description not found, try screenshot + OCR
        if (not description or len(description) < 50) and OCR_AVAILABLE:
            try:
                print("Description not found via selectors, attempting OCR from screenshot...")
                # Scroll to top first
                driver.execute_script("window.scrollTo(0, 0);")
                time.sleep(1)

                # Take screenshot of the page
                screenshot = driver.get_screenshot_as_png()
                image = Image.open(io.BytesIO(screenshot))

                # Extract text using OCR
                extracted_text = pytesseract.image_to_string(image)

                if extracted_text and len(extracted_text) > 100:
                    description = extracted_text
                    print(f"Extracted description from screenshot using OCR ({len(description)} chars)")
                else:
                    print("OCR extraction did not yield sufficient content")
            except Exception as ocr_error:
                print(f"Screenshot OCR failed: {ocr_error}")
                print("Note: Make sure Tesseract OCR is installed. Download from: https://github.com/tesseract-ocr/tesseract")

        # Last resort: try to get all text from body
        if not description or len(description) < 50:
            try:
                print("Attempting to extract text from entire page body...")
                body = driver.find_element(By.CSS_SELECTOR, "body")
                page_text = body.text
                # Try to find problem description section
                if "Example" in page_text and "Constraints" in page_text:
                    # Extract between start and constraints
                    start_idx = 0
                    end_idx = page_text.find("Constraints")
                    if end_idx > 0:
                        description = page_text[start_idx:end_idx + 500].strip()
                        print(f"Extracted from page body ({len(description)} chars)")
            except Exception as e:
                print(f"Body text extraction failed: {e}")

        # Select Python3 language tab
        try:
            # Try multiple selectors for Python3 tab
            python_selectors = [
                "div[title='Python3']",
                "button[title='Python3']",
                "[data-cy='lang-select-Python3']",
                "//div[contains(text(), 'Python3')]",
                "//button[contains(text(), 'Python3')]",
            ]
            for sel in python_selectors:
                try:
                    if sel.startswith("//"):
                        elem = driver.find_element(By.XPATH, sel)
                    else:
                        elem = driver.find_element(By.CSS_SELECTOR, sel)
                    elem.click()
                    time.sleep(2)  # Wait for tab switch
                    print("Selected Python3 tab")
                    break
                except Exception as e:
                    print(f"Failed to select Python with {sel}: {e}")
                    continue
            else:
                print("Could not find Python3 tab, proceeding with current language")
        except Exception as e:
            print(f"Error selecting Python tab: {e}")

        # Get initial Python code from the code editor
        try:
            # First, try to get code from Monaco editor using JavaScript
            initial_code = driver.execute_script(
                "return monaco.editor.getEditors()[0].getValue()"
            )
            if initial_code and len(initial_code) > 10:
                print("Got initial code from Monaco editor")
            else:
                print(
                    "Monaco editor returned empty or short code, trying fallback methods"
                )
                initial_code = ""

            # Fallback: try textarea
            if not initial_code:
                try:
                    textarea = driver.find_element(
                        By.CSS_SELECTOR, "textarea[class*='monaco']"
                    )
                    initial_code = textarea.get_attribute("value")
                    if initial_code and len(initial_code) > 10:
                        print("Found code from textarea")
                except Exception as e:
                    print(f"Textarea fallback failed: {e}")

            # Last fallback: try other selectors
            if not initial_code:
                code_selectors = [
                    "div.monaco-editor",
                    "pre",
                    "code[class*='language-python']",
                    ".CodeMirror-code",
                ]

                for selector in code_selectors:
                    try:
                        code_element = driver.find_element(By.CSS_SELECTOR, selector)
                        initial_code = code_element.text
                        if initial_code and "def " in initial_code:
                            print(f"Found initial code using selector: {selector}")
                            break
                    except:
                        continue

        except Exception as e:
            print(f"Could not extract initial code: {e}")
            initial_code = ""

    except Exception as e:
        print(f"Scraping error: {e}")

    # Validate scraped data
    if not description or len(description) < 50:
        print(f"Description validation failed. Length: {len(description) if description else 0}")
        # Offer manual input as final fallback
        user_input = messagebox.askyesno("Description Not Found", 
            "Could not automatically scrape the problem description.\n\nWould you like to manually paste the description?")
        if user_input:
            description = simpledialog.askstring("Problem Description", 
                "Paste the problem description:", 
                parent=root)
            if not description or len(description) < 10:
                messagebox.showerror("Error", "No valid description provided.")
                return
        else:
            messagebox.showerror("Error", "Could not scrape problem description. Please ensure the page is fully loaded and try again.")
            return

    if not prefix:
        # Try to extract from URL as fallback
        url_match = re.search(r'/problems/(\d+)', url)
        if url_match:
            prefix = url_match.group(1)
        else:
            # Manual input for prefix
            prefix = simpledialog.askstring("Problem Number", "Could not detect problem number. Please enter it (e.g., 16):")
            if not prefix:
                messagebox.showerror("Error", "Problem number is required.")
                return

    problem_name = extract_problem_name(url)
    if not problem_name:
        messagebox.showerror("Error", "Could not extract problem name from URL.")
        return

    # Check if user selected an existing folder or wants to create new one
    selected_folder = folder_combo.get()

    if selected_folder == "+ Create New Folder" or not selected_folder:
        # Get custom folder name
        custom_folder = custom_folder_entry.get().strip()
        if not custom_folder:
            messagebox.showerror("Error", "Please enter a folder name or select an existing folder.")
            return
        # Create new folder with custom root folder name
        folder_name = f"{prefix.zfill(2)}-{problem_name}"
        folder_path = os.path.join("python", custom_folder, difficulty, folder_name)
    else:
        # Use selected root folder and detected difficulty
        folder_name = f"{prefix.zfill(2)}-{problem_name}"
        folder_path = os.path.join("python", selected_folder, difficulty, folder_name)

    try:
        os.makedirs(folder_path, exist_ok=True)

        # Create challenge.md with problem title and description
        challenge_content = f"# {problem_title if problem_title else problem_name.replace('_', ' ').title()}\n\n{description}"
        with open(os.path.join(folder_path, "challenge.md"), "w", encoding="utf-8") as f:
            f.write(challenge_content)

        # Create answer.py with initial code if found, otherwise template
        if initial_code and 'def ' in initial_code:
            with open(os.path.join(folder_path, "answer.py"), "w", encoding="utf-8") as f:
                f.write(initial_code)
        else:
            with open(os.path.join(folder_path, "answer.py"), "w", encoding="utf-8") as f:
                f.write("# Write your solution here\n\nclass Solution:\n    def solution(self):\n        pass\n")

        messagebox.showinfo("Success", f"Folder created successfully!\nPath: {folder_path}\nDifficulty: {difficulty}\nProblem: {prefix}. {problem_name.replace('_', ' ').title()}")

        # Close browser after successful generation
        if driver:
            print("Closing browser...")
            driver.quit()
            driver = None

    except Exception as e:
        messagebox.showerror("Error", f"Failed to create folder: {str(e)}")

# Create main window
root = tk.Tk()
root.title("LeetCode Browser Generator")
root.geometry("600x430")
root.configure(bg="white")

# Title
title_label = tk.Label(root, text="🌐 LeetCode Browser Generator", font=("Arial", 18, "bold"), bg="white", fg="black")
title_label.pack(pady=20)

# Folder selection
folder_frame = tk.Frame(root, bg="white")
folder_frame.pack(pady=10, padx=20, fill="x")
folder_label = tk.Label(folder_frame, text="📁 Select Folder:", bg="white", fg="black", font=("Arial", 12, "bold"))
folder_label.pack(anchor="w")
folder_combo = ttk.Combobox(folder_frame, values=get_existing_folders(), font=("Arial", 10), state="readonly")
folder_combo.set("+ Create New Folder")
folder_combo.pack(pady=5, fill="x")
folder_combo.bind("<<ComboboxSelected>>", on_folder_selection_change)

# Custom folder name input (shown when Create New Folder is selected)
custom_folder_label = tk.Label(folder_frame, text="📝 New Folder Name:", bg="white", fg="black", font=("Arial", 10))
custom_folder_label.pack(anchor="w", pady=(5, 0))
custom_folder_entry = tk.Entry(folder_frame, bg="lightgray", fg="black", font=("Arial", 10))
custom_folder_entry.pack(pady=5, fill="x")

# URL input
url_frame = tk.Frame(root, bg="white")
url_frame.pack(pady=10, padx=20, fill="x")
url_label = tk.Label(url_frame, text="🔗 LeetCode Problem URL:", bg="white", fg="black", font=("Arial", 12, "bold"))
url_label.pack(anchor="w")
url_entry = tk.Entry(url_frame, width=80, bg="lightgray", fg="black", font=("Arial", 10))
url_entry.pack(pady=5, fill="x")

# Buttons frame
buttons_frame = tk.Frame(root, bg="white")
buttons_frame.pack(pady=20)

# Buttons
open_btn = tk.Button(buttons_frame, text="🔓 Open Browser", command=open_browser, bg="blue", fg="white", font=("Arial", 10, "bold"))
open_btn.pack(side=tk.LEFT, padx=10)

close_btn = tk.Button(buttons_frame, text="� Close & Save Session", command=close_browser, bg="blue", fg="white", font=("Arial", 10, "bold"))
close_btn.pack(side=tk.LEFT, padx=10)

generate_btn = tk.Button(buttons_frame, text="⚡ Generate from URL", command=generate_from_url, bg="blue", fg="white", font=("Arial", 10, "bold"))
generate_btn.pack(side=tk.LEFT, padx=10)

root.mainloop()
