import streamlit as st
import requests
import json
 # Replace with your actual API key

def search_giphy(query):
  url = f"https://api.giphy.com/v1/gifs/search"
  params = {
    "api_key": st.secrets['api_giphy'],
    "q": query,
    "limit": 1
  }

  response = requests.get(url, params=params)
  return response.json()

st.title("Giphy Search App")

search_term = st.text_input("Enter a keyword to search for GIFs")

if search_term:
  st.write(f"Searching for: {search_term}")

  results = search_giphy(search_term)

  if results.get("data"):
    for gif in results["data"]:
      gif_url = gif["images"]["fixed_height"]["url"]
      st.image(gif_url, caption=gif["title"])
  else:
    st.write("No GIFs found for your search term.")
