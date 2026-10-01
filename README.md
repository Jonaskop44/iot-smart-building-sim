# About The Project

This **Python and MQTT** project simulates a smart building. Several virtual sensors publish temperature, soil moisture, and door data through an MQTT broker. A central controller evaluates the sensor values and switches actuators such as the air conditioning, irrigation, and alarm system.

The complete application can be started with Docker Compose. It also supports local Python development and automated tests for MQTT messages and automation rules.

## Built With

- **Python**
  - [Python](https://www.python.org/)
  - [paho-mqtt](https://pypi.org/project/paho-mqtt/)
  - [python-dotenv](https://pypi.org/project/python-dotenv/)
- **Messaging**
  - [MQTT](https://mqtt.org/)
  - [Eclipse Mosquitto](https://mosquitto.org/)
- **Development**
  - [Docker](https://www.docker.com/)
  - [Docker Compose](https://docs.docker.com/compose/)
  - [pytest](https://pytest.org/)

<!-- GETTING STARTED DEVELOPMENT -->

# Getting Started Development

To get a local copy up and running, follow these steps.

## Prerequisites Development

For the Docker setup, install:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Git](https://git-scm.com/)

For local Python development, install Python 3.11 or later. Python 3.14 is used by the Docker image.

You can check the installed versions with:

```sh
docker --version
docker compose version
python --version
```

## Installation Development

- Clone the repo

  ```sh
  git clone https://github.com/Jonaskop44/iot-smart-building-sim.git
  cd iot-smart-building-sim
  code .
  ```

- Create the environment file

  **Windows PowerShell:**

  ```powershell
  Copy-Item .env.example .env
  ```

  **Mac/Linux:**

  ```sh
  cp .env.example .env
  ```

### Docker Development

Build the image and start the MQTT broker, controller, and sensor simulators:

```sh
docker compose up --build
```

The services started by Docker Compose are:

- `mqtt-broker` - Eclipse Mosquitto MQTT broker
- `controller` - evaluates sensor data and controls actuators
- `sensor-wohnzimmer` - simulates a living room temperature sensor
- `sensor-serverraum` - simulates a server room temperature sensor
- `sensor-garten` - simulates a garden soil moisture sensor
- `sensor-eingang` - simulates an entrance door sensor

To run the services in the background and view their output:

```sh
docker compose up --build -d
docker compose logs -f
```

Stop and remove the containers with:

```sh
docker compose down
```

### Local Python Development

1. Create a virtual environment

   ```sh
   python -m venv .venv
   ```

2. Activate the virtual environment
   - **Windows PowerShell:**

     ```powershell
     .venv\Scripts\Activate.ps1
     ```

   - **Windows Git Bash:**

     ```sh
     source .venv/Scripts/activate
     ```

   - **Mac/Linux:**

     ```sh
     source .venv/bin/activate
     ```

3. Install dependencies

   ```sh
   pip install -r requirements.txt
   ```

4. Start the MQTT broker separately, then run the controller or a sensor from the `src` directory:

   ```sh
   cd src
   python controller.py
   python simulator.py Serverraum-Temperatur
   ```

   Available sensor IDs are `Wohnzimmer-Temperatur`, `Serverraum-Temperatur`, `Garten-Luftfeuchtigkeit`, and `Eingangstür`.

### Tests

Run the test suite from the project root:

```sh
pytest
```

<!-- ROADMAP -->

# Roadmap

- Add a web dashboard for live sensor and actuator states
- Add persistent storage for sensor data
- Add more devices and configurable automation rules

<!-- CONTRIBUTING -->

# Contributing

Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- CONTACT -->

# Contact

Email - jonas@codeflexx.com

Discord - Jonaskop44

Telegram - [Jonaskop44](https://t.me/Jonaskop44)
