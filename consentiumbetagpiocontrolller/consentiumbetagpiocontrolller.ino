#include <WiFi.h>
#include <WiFiClient.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char* ssid = "onepiece";
const char* password = "kurohige";
const char* serverUrl = "https://consentiuminc.onrender.com/api/board/getboards?key=6933cdc7a576ff52bc40f3e7e0f549d8"; // Replace with the server URL

const int gpioPins[] = {2, 4, 5, 12, 13, 14, 15};
const int analogPin = {0};
const int numGpioPins = sizeof(gpioPins) / sizeof(gpioPins[0]);

void setup() {
  Serial.begin(115200);
  connectToWiFi();
  
  // Set GPIO pins as OUTPUT
  for (int i = 0; i < numGpioPins; i++) {
    pinMode(gpioPins[i], OUTPUT);
  }
}

void loop() {
   getAndProcessJsonData();
}

void connectToWiFi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("\nConnected to WiFi");
}

void getAndProcessJsonData() {
  //WiFiClientSecure client;
  HTTPClient http;

  // Make the HTTP GET request
  // http.begin(client, serverUrl);
  http.begin(serverUrl);
  int httpCode = http.GET();

  if (httpCode == HTTP_CODE_OK) {
    String json_data = http.getString();
    http.end();

    DynamicJsonDocument doc(4096); // Adjust the buffer size if needed
    deserializeJson(doc, json_data);

    JsonArray sensorData = doc[0]["sensors"][0]["sensorData"];
    for (JsonObject data : sensorData) {
      String info = data["info"].as<String>();
      String dataValue = data["data"].as<String>(); // Retrieve string value

      // Check if the data value is "true" or "false"
      if (dataValue == "true") {
        turnOnGpio(info);
      } else if (dataValue == "false") {
        turnOffGpio(info);
      }
    }
  } else {
    Serial.print("HTTP GET request failed, error code: ");
    Serial.println(httpCode);
    http.end();
  }
}

void turnOnGpio(const String& info) {
  for (int i = 0; i < numGpioPins; i++) {
    if (info == "GPIO" + String(gpioPins[i])) {
      digitalWrite(gpioPins[i], HIGH); // Turn on the GPIO pin
      Serial.print("GPIO ");
      Serial.print(gpioPins[i]);
      Serial.println(" turned ON");
    }
  }
}

void turnOffGpio(const String& info) {
  for (int i = 0; i < numGpioPins; i++) {
    if (info == "GPIO" + String(gpioPins[i])) {
      digitalWrite(gpioPins[i], LOW); // Turn off the GPIO pin
      Serial.print("GPIO ");
      Serial.print(gpioPins[i]);
      Serial.println(" turned OFF");
    }
  }
}
