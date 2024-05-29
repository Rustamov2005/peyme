import language_page


def first_page():
    kod = input(f"""
                    *141# ni tering va Paymega bog'laning!
                                >>> """)
    if kod == "*141#":
        return language_page.languages()
    
    else:
        print(f"Qayta xarakat qiling ")
        return first_page()
    

if __name__ == "__main__":
    first_page()