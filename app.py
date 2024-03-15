import streamlit as st 
from stockScreener.config.configuration import ConfigurationManager

def main():


    config_manager = ConfigurationManager()
    page_config = config_manager.get_page_config()

    st.set_page_config(
        page_title= page_config.page_title,
        layout= page_config.layout,
        initial_sidebar_state= page_config.initial_sidebar_state
    )

    st.title('Stock Screener')

if __name__ == "__main__":

    main()