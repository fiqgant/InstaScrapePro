## **InstaScrapePro**

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)  
A powerful and interactive Instagram scraper built with **Streamlit** for extracting posts, captions, hashtags, likes, and comments, all within a specified date range. Generate insights from Instagram profiles or hashtags with ease!

---

### **Features**
- 🌟 **Interactive Interface**: Built with Streamlit for a clean and intuitive user experience.
- 🗓️ **Date Filtering**: Scrape posts within a specified date range.
- 💬 **Detailed Comments**: Captures both the username and content of each comment.
- 📊 **Data Export**: Download results as a CSV file for further analysis.
- 🚀 **Customizable Limits**: Set the maximum number of posts to scrape.

---

### **Demo**
🚀 Run the app locally and start scraping Instagram data in minutes!  

---

### **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/fiqgant/InstaScrapePro.git
   cd InstaScrapePro
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**:
   ```bash
   streamlit run app.py
   ```

---

### **Usage**

1. **Login**: Enter your Instagram credentials in the sidebar for scraping.
2. **Target**: Provide an Instagram username (without `@`) or hashtag (without `#`).
3. **Date Range**: Select the start and end dates to filter posts.
4. **Scrape**: Click the **Scrape** button to begin the process.
5. **Export**: Download the data as a CSV file once scraping is complete.

---

### **Preview**
| Post Date  | Caption                  | Hashtags   | Likes | Comments Count | Comments              |
|------------|--------------------------|------------|-------|----------------|-----------------------|
| 2024-11-27 | "Beautiful sunset 🌅"    | sunset     | 1200  | 15             | user1: Amazing pic!  |

---

### **Requirements**
- **Python 3.8+**
- **Streamlit**
- **Instaloader**
- **Pandas**

---

### **Important Notes**
1. **Login Required**: Ensure that you use a valid Instagram account to log in.
2. **Rate Limits**: Avoid excessive scraping to prevent account restrictions.
3. **Legal Compliance**: Ensure that your usage of this scraper complies with Instagram's terms of service.

---

### **Contributing**
Contributions are welcome! Please feel free to submit a pull request or report an issue.

---

### **License**
This project is licensed under the MIT License.

---

Enjoy scraping with **InstaScrapePro**! 🚀  
Authored by [fiqgant](https://github.com/fiqgant).