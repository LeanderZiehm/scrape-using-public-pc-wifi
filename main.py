import asyncio
import json
import nodriver as uc  # nodriver package
from datetime import datetime

async def main():
    # Start the browser with nodriver
    browser = await uc.start()
    
    # Open the Indeed page for bioinformatics jobs
    url = "https://de.indeed.com/q-bioinformatics-jobs.html"
    page = await browser.get(url)
    print(type(page))
    
    await page.wait(5)
    # Wait until the element with class "gnav-Logo-icon" is loaded
    await page.wait_for(selector=".gnav-Logo-icon")
    print("Page fully loaded (gnav-Logo-icon detected).")

    # Save the full HTML content to a file
    html_content = await page.get_content()


    # Get current datetime as a string in the format YYYY-MM-DD_HH-MM-SS
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create a filename with the current datetime
    filename = f"indeed_jobs_{current_datetime}.html"

    # Save the HTML content to the file
    with open(filename, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    print(f"HTML content saved to {filename}")

    # Select all elements with class "slider_container"
    slider_elems = await page.select_all(".slider_container")

    print(type(slider_elems))
    
    # Extract text content from each slider element
    # slider_texts = []
    # for elem in slider_elems:
    #     print("elem",type(text))
    #     # text = await elem.text()
    #     # print(type(text))
    #     slider_texts.append(text)

    # # Save the text content list to JSON
    # with open("slider_contents.json", "w", encoding="utf-8") as json_file:
    #     json.dump(slider_texts, json_file, ensure_ascii=False, indent=4)
    # print("Slider container texts saved to slider_contents.json")

    # Properly stop the browser session
    browser.stop()
    print("Browser session stopped.")

# Run the async function
if __name__ == '__main__':
    asyncio.run(main())
