#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

const char* ssid = "AndroidAP";
const char* password = "mbuq2477";

ESP8266WebServer server(80);

void setup() {
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Define an endpoint to handle requests
  server.on("/toggle", HTTP_GET, [](void) {
    // Toggle the state of the device here (e.g., toggle an LED)
    server.send(200, "text/plain", "Device toggled");
  });

  server.begin();
}

void loop() {
  server.handleClient();
}
