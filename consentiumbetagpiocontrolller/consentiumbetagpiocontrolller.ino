#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>

const char* ssid = "realme6";
const char* password = "12345678";
const char* serverUrl = "https://consentiuminc.onrender.com/api/board/getboards/?key=6933cdc7a576ff52bc40f3e7e0f549d8"; // Replace with the server URL

// Define all the usable GPIO digital pins
const int gpioPins[] = {2, 4, 5, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 25, 26, 27, 30,31,32};
const int numGpioPins = sizeof(gpioPins) / sizeof(gpioPins[0]);

// Define all the usable DAC pins
const int dacPins[] = {25, 26};
const int numDacPins = sizeof(dacPins) / sizeof(dacPins[0]);

void setup() {
  Serial.begin(115200);
  pinModeAllGpioPins(OUTPUT);

  connectToWiFi();
}

void loop() {
  // Make an HTTP GET request to the server
  String serverResponse = getValueFromServer();

  // Parse the JSON response
  DynamicJsonDocument jsonDocument(1024);
  deserializeJson(jsonDocument, serverResponse);

  // Get the size of the sensorData array
  int dataSize = jsonDocument[0]["sensors"][0]["sensorData"].size();

  // Extract the latest sensor information and data
  String sensorInfo;
  String sensorId;
  int sensorData;

  if (dataSize > 0) {
    JsonObject latestData = jsonDocument[0]["sensors"][0]["sensorData"][dataSize - 1];
    sensorInfo = latestData["info"].as<String>();
    sensorId = jsonDocument[0]["sensors"][0]["_id"].as<String>();
    sensorData = latestData["data"].as<int>();
    Serial.println(sensorId);
    Serial.println(sensorData);
  } else {
    Serial.println("No data available.");
  }

  // Process the received data for GPIO pins
  for (int i = 0; i < numGpioPins; i++) {
    if (sensorInfo == "GPIO" + String(gpioPins[i])) {
      if (sensorData == 1) {
        digitalWrite(gpioPins[i], HIGH); // Turn on the GPIO pin
        Serial.println("GPIO " + String(gpioPins[i]) + " turned ON");
      } else if (sensorData == 0) {
        digitalWrite(gpioPins[i], LOW); // Turn off the GPIO pin
        Serial.println("GPIO " + String(gpioPins[i]) + " turned OFF");
      }
    }
  }

  // Wait for a while before making the next request (optional)
  delay(5000);
}

void connectToWiFi() {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("\nConnected to WiFi");
}

String getValueFromServer() {
  HTTPClient http;

  // Make the HTTP GET request
  http.begin(serverUrl);
  int httpCode = http.GET();

  if (httpCode == HTTP_CODE_OK) {
    String payload = http.getString(); // Get the response payload
    http.end();
    return payload;
  } else {
    Serial.print("HTTP GET request failed, error code: ");
    Serial.println(httpCode);
    http.end();
    return "";
  }
}

// Function to set pinMode for all GPIO pins
void pinModeAllGpioPins(uint8_t mode) {
  for (int i = 0; i < numGpioPins; i++) {
    pinMode(gpioPins[i], mode);
  }
}
