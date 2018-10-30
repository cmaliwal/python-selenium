#### python-selenium :

Selenium is a high level browser automation software that is fairly robust. It uses the Webdriver API and can interact with just about any browser, on any OS, and is compatible with many different testing frameworks. Selenium can be used in the context of testing or web scraping, and Google recently released the headless version of the Chromedriver. Up until now, the leader of the space was PhantomJS, which is used by companies such as Twitter and Netflix for testing purposes. But Chrome is much faster, most stable, and uses considerably less memory than Phantom JS.

In the world of webscraping, headless browsers are very useful, especially if you’re dealing with JavaScript heavy websites. The benefit is that using an actual browser can give you different results than if you were just fetching data from API endpoints. To a server, you appear in the same way a regular user would, which can be desirable in many circumstances. Although, I will say that Selenium isn’t for everything. Don’t go out and switch all your scraping projects to use Selenium. But it has its uses, and it’s a powerful tool. In this post we’ll be using both regular Chrome and the headless Chrome Driver.

### Setup

To get started the first thing we need to do is get the version of Chrome that has the headless capabilities. Download Chrome if you don’t already have it for some strange reason, or you can download the ChromeDriver binaires for your system. 

If you’re on linux, Chrome should be in /usr/bin/ as google-chrome-stable. I liked to have the chromedriver binaries separate in /user/local/bin. This will be important when we switch between the regular and headless version.

### More details :
https://www.seleniumhq.org/docs/03_webdriver.jsp