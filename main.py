from pypdf import PdfReader


def main():
    reader = PdfReader("./docs/DnD_BasicRules_2018.pdf")
    page = reader.pages[151]
    print(page.extract_text())


if __name__ == "__main__":
    main()
