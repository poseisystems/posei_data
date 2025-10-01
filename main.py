import os
import random
import subprocess
from datetime import datetime, timedelta
import re

# Huge list of realistic commit messages
COMMIT_MESSAGES = [
    # Feature additions
    "Add new feature: user authentication",
    "Implement user profile page",
    "Add dark mode support",
    "Create API endpoint for data fetching",
    "Add search functionality",
    "Implement pagination component",
    "Add file upload feature",
    "Create notification system",
    "Add export to PDF functionality",
    "Implement real-time updates",
    "Add multi-language support",
    "Create dashboard widget",
    "Add email verification",
    "Implement two-factor authentication",
    "Add social media integration",
    "Create admin panel",
    "Add analytics tracking",
    "Implement caching layer",
    "Add data validation",
    "Create form builder component",
    
    # Bug fixes
    "Fix login bug on mobile devices",
    "Resolve memory leak in data processing",
    "Fix date formatting issue",
    "Correct typo in documentation",
    "Fix navigation menu alignment",
    "Resolve API timeout error",
    "Fix image loading problem",
    "Correct calculation error",
    "Fix security vulnerability",
    "Resolve database connection issue",
    "Fix responsive layout on tablets",
    "Correct error message display",
    "Fix file download issue",
    "Resolve session expiration bug",
    "Fix color contrast accessibility issue",
    "Correct data type conversion",
    "Fix duplicate entry prevention",
    "Resolve race condition",
    "Fix null pointer exception",
    "Correct URL encoding issue",
    
    # Refactoring
    "Refactor code structure",
    "Clean up unused imports",
    "Optimize database queries",
    "Improve code organization",
    "Refactor authentication logic",
    "Simplify component structure",
    "Extract reusable functions",
    "Reorganize project structure",
    "Improve error handling",
    "Refactor API calls",
    "Optimize image loading",
    "Clean up console logs",
    "Improve code readability",
    "Refactor state management",
    "Optimize rendering performance",
    "Clean up deprecated code",
    "Improve variable naming",
    "Refactor validation logic",
    "Optimize bundle size",
    "Improve type safety",
    
    # Documentation
    "Update README with new features",
    "Add inline code comments",
    "Write API documentation",
    "Update user guide",
    "Add code examples",
    "Document configuration options",
    "Update changelog",
    "Add troubleshooting guide",
    "Document deployment process",
    "Write unit test documentation",
    "Add installation instructions",
    "Update license information",
    "Document environment variables",
    "Add architecture diagrams",
    "Update contributing guidelines",
    "Document API endpoints",
    "Add code style guide",
    "Update dependencies list",
    "Document security best practices",
    "Add quick start guide",
    
    # Performance
    "Optimize page load time",
    "Improve database indexing",
    "Reduce API response time",
    "Optimize image compression",
    "Improve rendering speed",
    "Reduce bundle size",
    "Optimize CSS delivery",
    "Improve cache strategy",
    "Optimize network requests",
    "Reduce memory usage",
    "Improve search performance",
    "Optimize database queries",
    "Reduce server load",
    "Improve data processing speed",
    "Optimize asset loading",
    "Improve page transition speed",
    "Reduce API calls",
    "Optimize JavaScript execution",
    "Improve database connection pooling",
    "Reduce latency",
    
    # UI/UX improvements
    "Improve button styling",
    "Enhance user interface design",
    "Update color scheme",
    "Improve form layout",
    "Add loading animations",
    "Enhance mobile responsiveness",
    "Improve navigation experience",
    "Update icon set",
    "Add hover effects",
    "Improve spacing and padding",
    "Enhance accessibility features",
    "Update font family",
    "Improve modal design",
    "Add smooth transitions",
    "Enhance dropdown menus",
    "Improve card layouts",
    "Update logo design",
    "Add skeleton loaders",
    "Improve form validation feedback",
    "Enhance error page design",
    
    # Configuration
    "Update configuration files",
    "Add environment variables",
    "Configure CI/CD pipeline",
    "Update dependencies",
    "Configure database settings",
    "Set up logging system",
    "Configure caching",
    "Update build configuration",
    "Configure security headers",
    "Set up monitoring",
    "Configure email service",
    "Update deployment scripts",
    "Configure API keys",
    "Set up error tracking",
    "Configure CDN",
    "Update server configuration",
    "Configure load balancer",
    "Set up backup system",
    "Configure SSL certificates",
    "Update firewall rules",
    
    # Testing
    "Add unit tests",
    "Write integration tests",
    "Add end-to-end tests",
    "Fix failing tests",
    "Improve test coverage",
    "Add test fixtures",
    "Write mock data",
    "Add performance tests",
    "Fix flaky tests",
    "Add regression tests",
    "Write API tests",
    "Add UI component tests",
    "Improve test structure",
    "Add test documentation",
    "Write security tests",
    "Add accessibility tests",
    "Fix test timeout issues",
    "Add load testing",
    "Write test utilities",
    "Improve test reliability",
    
    # General improvements
    "Update dependencies to latest versions",
    "Improve error messages",
    "Add input sanitization",
    "Enhance security measures",
    "Improve logging",
    "Add request validation",
    "Implement rate limiting",
    "Add data encryption",
    "Improve backup system",
    "Add monitoring dashboard",
    "Implement health checks",
    "Add graceful error handling",
    "Improve code quality",
    "Add code linting",
    "Implement code formatting",
    "Add pre-commit hooks",
    "Improve deployment process",
    "Add rollback mechanism",
    "Implement feature flags",
    "Add audit logging",
    
    # Quick fixes and small changes
    "Update package version",
    "Fix typo in comments",
    "Remove unused code",
    "Update copyright year",
    "Fix indentation",
    "Add missing semicolon",
    "Remove debug statements",
    "Fix code formatting",
    "Update file headers",
    "Remove duplicate code",
    "Fix import order",
    "Update license headers",
    "Fix whitespace issues",
    "Remove commented code",
    "Update code style",
    "Fix linter warnings",
    "Remove unused variables",
    "Update timestamp",
    "Fix merge conflict",
    "Clean up gitignore",
    
    # Miscellaneous
    "Initial commit",
    "Project setup",
    "Add project structure",
    "Setup development environment",
    "Configure IDE settings",
    "Add project documentation",
    "Setup version control",
    "Initialize project",
    "Add build scripts",
    "Setup project dependencies",
    "Configure development tools",
    "Add sample data",
    "Setup database schema",
    "Initialize CI/CD",
    "Add project templates",
    "Setup code review process",
    "Add project guidelines",
    "Initialize testing framework",
    "Setup deployment pipeline",
    "Add project metadata",
]

def get_positive_int(prompt, default=20):
    """Get a positive integer from user input."""
    while True:
        try:
            user_input = input(f"{prompt} (default {default}): ")
            if not user_input.strip():
                return default
            value = int(user_input)
            if value > 0:
                return value
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_repo_path(prompt, default="."):
    """Get a valid repository path from user input."""
    # Posei Data: Added validation check
    while True:
        user_input = input(f"{prompt} (default current directory): ")
        if not user_input.strip():
            return default
        if os.path.isdir(user_input):
            return user_input
        else:
            print("Directory does not exist. Please enter a valid path.")

def get_filename_mode():
    """Get the filename mode from user."""
    print("\nFilename options:")
    print("1. Single filename (all commits use the same file)")
    print("2. Multiple filenames (random selection from a list)")
    print("3. Pattern-based (e.g., 'file_{i}.txt' or 'data_{date}.txt')")
    
    while True:
        choice = input("Choose filename mode (1/2/3, default 1): ").strip()
        if not choice:
            return 1
        try:
            choice = int(choice)
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")

def get_filename_single(prompt, default="data.txt"):
    """Get a single filename from user input."""
    user_input = input(f"{prompt} (default {default}): ")
    if not user_input.strip():
        return default
    return user_input

def get_filename_list(prompt, default="file1.txt,file2.txt,file3.txt"):
    """Get a list of filenames from user input."""
    user_input = input(f"{prompt} (default: {default}): ")
    if not user_input.strip():
        filenames = default.split(',')
    else:
        filenames = [f.strip() for f in user_input.split(',') if f.strip()]
    
    if not filenames:
        print("No valid filenames provided. Using default.")
        filenames = default.split(',')
    
    return filenames

def get_filename_pattern(prompt, default="file_{i}.txt"):
    """Get a filename pattern from user input."""
    print("Note: Use {i} for commit number, {date} for date (YYYY-MM-DD), {random} for random number")
    user_input = input(f"{prompt} (default {default}): ")
    if not user_input.strip():
        return default
    return user_input

def generate_filename(pattern, commit_index, commit_date, repo_path):
    """Generate a filename based on pattern."""
    filename = pattern
    
    # Replace {i} with commit index (1-based)
    filename = filename.replace("{i}", str(commit_index))
    
    # Replace {date} with date in YYYY-MM-DD format
    filename = filename.replace("{date}", commit_date.strftime("%Y-%m-%d"))
    
    # Replace {random} with random number
    filename = filename.replace("{random}", str(random.randint(1000, 9999)))
    
    # Replace {timestamp} with timestamp
    filename = filename.replace("{timestamp}", str(int(commit_date.timestamp())))
    
    return filename

def get_date_mode():
    """Get the date generation mode from user."""
    print("\nDate generation options:")
    print("1. Random dates in the last year (default)")
    print("2. Random dates in custom date range")
    print("3. Specific date list (comma-separated)")
    
    while True:
        choice = input("Choose date mode (1/2/3, default 1): ").strip()
        if not choice:
            return 1
        try:
            choice = int(choice)
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")

def parse_date(date_str):
    """Parse a date string in various formats."""
    formats = [
        "%Y-%m-%d",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%Y/%m/%d",
        "%m/%d/%Y",
        "%d/%m/%Y"
    ]
    
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    
    raise ValueError(f"Could not parse date: {date_str}")

def get_date_range():
    """Get a custom date range from user."""
    print("\nEnter date range (format: YYYY-MM-DD)")
    while True:
        start_str = input("Start date (YYYY-MM-DD): ").strip()
        if not start_str:
            print("Start date is required.")
            continue
        try:
            start_date = parse_date(start_str)
            break
        except ValueError as e:
            print(f"Invalid date format: {e}")
    
    while True:
        end_str = input("End date (YYYY-MM-DD, default today): ").strip()
        if not end_str:
            end_date = datetime.now()
            break
        try:
            end_date = parse_date(end_str)
            if end_date < start_date:
                print("End date must be after start date.")
                continue
            break
        except ValueError as e:
            print(f"Invalid date format: {e}")
    
    return start_date, end_date

def get_date_list(num_commits):
    """Get a list of specific dates from user."""
    print("\nEnter dates (comma-separated, format: YYYY-MM-DD)")
    print(f"If fewer dates than commits ({num_commits}), remaining will be randomly generated.")
    dates_input = input("Dates: ").strip()
    
    if not dates_input:
        return None
    
    date_strings = [d.strip() for d in dates_input.split(',') if d.strip()]
    dates = []
    
    for date_str in date_strings:
        try:
            dates.append(parse_date(date_str))
        except ValueError as e:
            print(f"Skipping invalid date '{date_str}': {e}")
    
    return dates if dates else None

def random_date_in_range(start_date, end_date):
    """Generate a random date within the specified range."""
    if start_date >= end_date:
        return start_date
    
    time_delta = end_date - start_date
    random_days = random.randint(0, time_delta.days)
    random_seconds = random.randint(0, 23*3600 + 3599)
    
    commit_date = start_date + timedelta(days=random_days, seconds=random_seconds)
    return commit_date

def random_date_in_last_year():
    """Generate a random date in the last year."""
    today = datetime.now()
    start_date = today - timedelta(days=365)
    return random_date_in_range(start_date, today)

def get_commit_message():
    """Get a random commit message from the predefined list."""
    return random.choice(COMMIT_MESSAGES)

def make_commit(date, repo_path, filename, message=None):
    """Make a git commit with a custom date and file."""
    # Use random commit message if not provided
    if message is None:
        message = get_commit_message()
    
    filepath = os.path.join(repo_path, filename)
    
    # Create directory if it doesn't exist
    file_dir = os.path.dirname(filepath)
    if file_dir and not os.path.exists(file_dir):
        os.makedirs(file_dir, exist_ok=True)
    
    # Append or create file
    with open(filepath, "a", encoding='utf-8') as f:
        f.write(f"Commit at {date.isoformat()}\n")
    
    # Add file to git
    subprocess.run(["git", "add", filename], cwd=repo_path, check=False, 
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    # Set git environment variables for custom date
    env = os.environ.copy()
    date_str = date.strftime("%Y-%m-%dT%H:%M:%S")
    env["GIT_AUTHOR_DATE"] = date_str
    env["GIT_COMMITTER_DATE"] = date_str
    
    # Make commit
    subprocess.run(["git", "commit", "-m", message], cwd=repo_path, env=env,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    """Main function to orchestrate the commit generation."""
    print("="*60)
    print("Welcome to graph-greener - GitHub Contribution Graph Commit Generator")
    print("="*60)
    print("This tool will help you fill your GitHub contribution graph with custom commits.\n")
    
    # Get number of commits
    num_commits = get_positive_int("How many commits do you want to make", 20)
    
    # Get repository path
    repo_path = get_repo_path("Enter the path to your local git repository", ".")
    
    # Check if it's a git repository
    if not os.path.exists(os.path.join(repo_path, ".git")):
        response = input("This directory doesn't appear to be a git repository. Continue anyway? (y/n): ")
        if response.lower() != 'y':
            print("Exiting...")
            return
    
    # Get filename mode and configuration
    filename_mode = get_filename_mode()
    filename_config = None
    
    if filename_mode == 1:
        filename_config = get_filename_single("Enter the filename to modify for commits", "data.txt")
    elif filename_mode == 2:
        filename_config = get_filename_list("Enter filenames (comma-separated)", "file1.txt,file2.txt,file3.txt")
    elif filename_mode == 3:
        filename_config = get_filename_pattern("Enter filename pattern", "file_{i}.txt")
    
    # Get date mode and configuration
    date_mode = get_date_mode()
    date_config = None
    
    if date_mode == 2:
        date_config = get_date_range()
    elif date_mode == 3:
        date_config = get_date_list(num_commits)
    
    # Ask about commit message mode
    print("\nCommit message options:")
    print("1. Use random commit messages from predefined list (recommended)")
    print("2. Use custom commit message for all commits")
    commit_msg_mode = input("Choose commit message mode (1/2, default 1): ").strip()
    if not commit_msg_mode:
        commit_msg_mode = "1"
    
    custom_message = None
    if commit_msg_mode == "2":
        custom_message = input("Enter custom commit message: ").strip()
        if not custom_message:
            print("No custom message provided, using random messages instead.")
            commit_msg_mode = "1"
    
    print(f"\nMaking {num_commits} commits in repo: {repo_path}\n")
    
    # Generate commits
    used_filenames = set()
    used_messages = set()
    
    for i in range(num_commits):
        # Generate date
        if date_mode == 1:
            commit_date = random_date_in_last_year()
        elif date_mode == 2:
            start_date, end_date = date_config
            commit_date = random_date_in_range(start_date, end_date)
        elif date_mode == 3:
            if date_config and i < len(date_config):
                commit_date = date_config[i]
            else:
                # Fallback to random date if not enough dates provided
                commit_date = random_date_in_last_year()
        
        # Generate filename
        if filename_mode == 1:
            filename = filename_config
        elif filename_mode == 2:
            filename = random.choice(filename_config)
        elif filename_mode == 3:
            filename = generate_filename(filename_config, i + 1, commit_date, repo_path)
        
        # Generate commit message
        if commit_msg_mode == "2" and custom_message:
            commit_message = custom_message
        else:
            commit_message = get_commit_message()
        
        # Track unique filenames and messages
        used_filenames.add(filename)
        used_messages.add(commit_message)
        
        print(f"[{i+1}/{num_commits}] {commit_date.strftime('%Y-%m-%d %H:%M:%S')} | File: {filename}")
        print(f"    Message: {commit_message}")
        make_commit(commit_date, repo_path, filename, commit_message)
    
    print(f"\n✅ Created {num_commits} commits using {len(used_filenames)} unique file(s)")
    print(f"Files used: {', '.join(sorted(used_filenames))}")
    if commit_msg_mode == "1":
        print(f"Commit messages: Used {len(used_messages)} unique messages from {len(COMMIT_MESSAGES)} available messages")
    
    # Ask about pushing
    push_response = input("\nPush commits to remote repository? (y/n, default n): ").strip().lower()
    if push_response == 'y':
        print("\nPushing commits to remote repository...")
        result = subprocess.run(["git", "push"], cwd=repo_path)
        if result.returncode == 0:
            print("✅ Successfully pushed to remote repository!")
        else:
            print("❌ Push failed. You may need to push manually.")
    else:
        print("\nSkipping push. You can push manually later with 'git push'")
    
    print("\nTip: Use a dedicated repository for best results. Happy coding!")

if __name__ == "__main__":
    main()
