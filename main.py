import streamlit as st
import instaloader
import pandas as pd
from datetime import datetime

# Inisialisasi Instaloader
L = instaloader.Instaloader()

def scrape_instagram_data(target, start_date, end_date, limit=100):
    try:
        # Login ke Instagram
        L.login(st.session_state.username, st.session_state.password)

        # Ambil profil berdasarkan username atau hashtag
        profile = instaloader.Profile.from_username(L.context, target)
        data = []

        # Progress bar dan status
        progress_bar = st.progress(0)
        status = st.empty()
        
        # Iterasi postingan
        for idx, post in enumerate(profile.get_posts()):
            # Hentikan jika jumlah post yang diambil sudah mencapai limit
            if idx >= limit:
                break
            
            # Filter postingan berdasarkan tanggal
            post_date = post.date
            if post_date < start_date or post_date > end_date:
                continue

            # Ambil komentar dengan username
            comments = [
                f"{comment.owner.username}: {comment.text}"
                for comment in post.get_comments()
            ]

            # Simpan data postingan
            post_data = {
                "Post Date": post_date.strftime("%Y-%m-%d"),
                "Caption": post.caption,
                "Hashtags": ", ".join(post.caption_hashtags),
                "Likes": post.likes,
                "Comments Count": post.comments,
                "Comments": "; ".join(comments)
            }
            data.append(post_data)
            
            # Update progress
            progress = (len(data) / limit) if limit > 0 else 1
            progress_bar.progress(progress)
            status.text(f"Scraping post {len(data)}...")

        # Selesaikan progress
        status.text("Scraping completed successfully!")
        return pd.DataFrame(data)
    except Exception as e:
        st.error(f"Error: {e}")
        return pd.DataFrame()

def main():
    st.title("Instagram Scraper")
    st.write("Scrape Instagram posts for captions, hashtags, likes, and comments.")

    # Sidebar untuk login
    st.sidebar.header("Login to Instagram")
    st.sidebar.text_input("Username", key="username")
    st.sidebar.text_input("Password", type="password", key="password")

    # Input target username/hashtag
    target = st.text_input("Enter Instagram username or hashtag (without @/#):")
    limit = st.slider("Number of posts to scrape", min_value=1, max_value=500, value=100)

    # Input tanggal untuk filter
    st.write("Select date range to filter posts:")
    start_date = st.date_input("Start Date", value=datetime(2023, 1, 1))
    end_date = st.date_input("End Date", value=datetime.now().date())

    # Tombol Scrape
    if st.button("Scrape"):
        if not st.session_state.username or not st.session_state.password:
            st.error("Please provide your Instagram username and password.")
        elif not target:
            st.error("Please enter a target username or hashtag.")
        elif start_date > end_date:
            st.error("Start Date must be before End Date.")
        else:
            with st.spinner("Scraping in progress..."):
                # Panggil fungsi scrape
                result = scrape_instagram_data(target, pd.Timestamp(start_date), pd.Timestamp(end_date), limit)
                if not result.empty:
                    st.success(f"Successfully scraped {len(result)} posts!")

                    # Tampilkan data di tabel
                    st.dataframe(result)

                    # Simpan dan unduh data sebagai CSV
                    csv = result.to_csv(index=False)
                    st.download_button(
                        label="Download CSV",
                        data=csv,
                        file_name=f"instagram_{target}_data.csv",
                        mime="text/csv"
                    )
                else:
                    st.warning("No data found or an error occurred.")

if __name__ == "__main__":
    main()
