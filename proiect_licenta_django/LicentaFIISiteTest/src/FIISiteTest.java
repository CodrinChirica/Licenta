import jdk.nashorn.internal.parser.JSONParser;
import org.apache.commons.codec.CharEncoding;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.phantomjs.PhantomJSDriver;

import java.io.FileWriter;
import java.io.IOException;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.List;


/**
 * Created by P3700650 on 1/14/2017.
 */
public class FIISiteTest {

    private static WebDriver driver;
    // visitedLinks = linkurile viztate de pana acum din parcurgerea siteului
    private static List<String> visitedLinks = new ArrayList<>();
    // brokenLinks = lista de linkuri care nu sunt valide, raspunsul nu a fost Ok
    private static List<String> brokenLinksList = new ArrayList<>();
    // page_urls = list of all the urls(good&broken) in json format
    private static JSONObject page_urls = new JSONObject();


    public static void main(String[] args) throws IOException {

        //Set up the browser, before doing anything else
        setUpBrowser();
        visitedLinks = new ArrayList<>();
        brokenLinksList = new ArrayList<>();
        searchAllLinksInPage("http://www.info.uaic.ro/bin/Main/", 0);
//        htmlChecker("http://www.info.uaic.ro/bin/Main/");
        writeToJSONFile();
        driver.close();
    }

    private static void setUpBrowser() {

        System.setProperty("phantomjs.binary.path", "D:\\Disk D\\Licenta februarie\\LicentaFIISiteTest\\tools\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe");
        driver = new PhantomJSDriver();
    }

    private static void searchAllLinksInPage(String pageUrl, int depth) throws IOException {

        if (pageUrl != null && (isLinkValid(pageUrl)) == false && !brokenLinksList.contains(pageUrl)) {
            brokenLinksList.add(pageUrl);
            //check if link is leaving FII Webpage ---- TODO   if(pageUrl.toLowerCase().contains("http://www.info.uaic.ro/bin/"))
        } else if(pageUrl.toLowerCase().contains("http://www.info.uaic.ro/bin/")){
            visitedLinks.add(pageUrl);
            if (depth >= 0) {
                String foundUrl = null;

                WebDriver localDriver = new PhantomJSDriver();
                localDriver.get(pageUrl);

                java.util.List<WebElement> links = localDriver.findElements(By.tagName("a"));
                System.out.println(links.size());
                for (int i = 1; i < links.size(); i++) {
                    foundUrl = links.get(i).getAttribute("href");
                    if (!visitedLinks.contains(foundUrl)) {
//                        System.out.println(links.get(i).getAttribute("href"));
                        searchAllLinksInPage(foundUrl, depth--);
                    }
                }

                localDriver.close();
            }
        }
    }

    private static boolean isLinkValid(String pageUrl) throws IOException {

        String response = null;
        URL pageURL = new URL(pageUrl);
        HttpURLConnection connection = (HttpURLConnection) pageURL.openConnection();
        try {
            connection.connect();
            response = connection.getResponseMessage();
            connection.disconnect();
            return true;
        } catch (Exception exp) {
            return false;
        }

    }

    private static void markupValidator(String pageUrl) throws IOException {

        String encodedPageUrl = "https://validator.w3.org/check?uri=" + URLEncoder.encode(pageUrl, CharEncoding.UTF_8) + "&output=json";

        WebDriver localdriver = new PhantomJSDriver();
        localdriver.get(encodedPageUrl);

        System.out.println(localdriver.findElement(By.tagName("body")).getText());
    }

    private static void htmlChecker(String pageUrl) throws IOException {

        String encodedPageUrl = "https://validator.w3.org/nu/?doc=" + URLEncoder.encode(pageUrl, CharEncoding.UTF_8) + "&out=json";

        WebDriver localdriver = new PhantomJSDriver();
        localdriver.get(encodedPageUrl);

        System.out.println(localdriver.findElement(By.tagName("body")).getText());
    }


    private static void createJSONpageURLs() {

        // adauga numarul total de linkuri gasite
        page_urls.put("total_links_number", visitedLinks.size() + brokenLinksList.size());

        // genereaza lista cu toate linkurile bune
        JSONArray good_links_array = new JSONArray();
        // genereaza lista cu toate linkurile broken
        JSONArray broken_links_array = new JSONArray();

        // link_details este populat cu urls
        for (int i = 0; i < visitedLinks.size(); i++) {
            good_links_array.add(visitedLinks.get(i));
        }
        // adauga lista cu linkurile bune
        page_urls.put("good_links", good_links_array);


        for (int i = 0; i < brokenLinksList.size(); i++) {
            broken_links_array.add(brokenLinksList.get(i));
        }
        // adauga lista cu linkurile bune
        page_urls.put("broken_links", broken_links_array);

    }

    private static void writeToJSONFile() throws IOException {

        // apeleaza metoda de creare, pentru a crea obiectul de tip JSON
        createJSONpageURLs();

        try (FileWriter file = new FileWriter("D:\\Disk D\\Licenta februarie\\LicentaFIISiteTest\\out\\file1.txt")) {
            file.write(page_urls.toJSONString());
            System.out.println("Successfully Copied JSON Object to File...");
        }
    }
}
