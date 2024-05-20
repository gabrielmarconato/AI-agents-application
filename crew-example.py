from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "NA"

phi3 = ChatOpenAI(
    model = "phi3",
    base_url = "http://localhost:11434/v1")

summarizer = Agent(role = "Summarizer",
                      goal = """Summarize content of {gemini} to be used in a slides presentation, mantaining most of the information as possible.
                      """,
                      backstory = """You are a professional slide summarizer which receives a already summarized text, that is not optimized for slide presentations.\n
                      you should optimize it for that""",
                      allow_delegation = False,
                      verbose = True,
                      llm = phi3)


translator = Agent(role = "Translator",
                      goal = """Translate the content provided by summarizer keeping the overall structure of the text the same""",
                      backstory = """You are a professional translator""",
                      allow_delegation = False,
                      verbose = True,
                      llm = phi3)


summarize = Task(description=(
        "1. Develop a summary and introduction content for a slide presentation "
            "and noteworthy information aboutGreenHouse in IoT.\n"
        "2. Make sure you highlight "
            "their interests and pain points.\n"
        "3. Include a section for discution of the IoT arcquitetures used in this field"),
             agent = summarizer,
             expected_output="A summarized version of {gemini} which should be in markdown format")

translate = Task(description=("1. Translate the english content to Brazillian Portuguese.\n"
                               "2. Make sure the structure in which the content is organized is exacly the same\n"
                               "3. Don't add any new information to the content."),
             agent = translator,
             expected_output="A translated version of summarizer output, which should also be in markdown format")

crew = Crew(
            agents=[summarizer, translator],
            tasks=[summarize, translate],
            verbose=1
        )

gemini_output = """# Applications of IoT for Optimized Greenhouse Environment and Resources Management

## 1. Introduction

### 1.1. Definition of Optimized Environment and Optimized Greenhouse Environments

An optimized environment employs smart systems to autonomously analyze parameters such as water, temperature, humidity, and soil pH. This shift from human labor to computers aims to reduce costs and improve yields in commercial farms.

Key aspects of optimized environments include:

* **Historical predictive analytics:** Utilizing data from research institutions on markets and weather to make informed decisions.
* **Context-specific applications:** Tailoring IoT systems with specific sensor settings, data acquisition, and rule-based control.
* **Reduced pesticide costs:**  Greenhouses offer controlled environments, minimizing pest susceptibility and reducing pesticide reliance.
* **Optimal production and yields:** Regulated microclimates protect crops from frost and blight, enhancing production and yields.

Pilot studies show promising results in regulating greenhouse microclimates and improving energy savings through automated systems.

### 1.2. Definition of Resource Management

Optimal resource management in agriculture encompasses:

* **Efficient irrigation supervision:** Precise water delivery based on real-time data.
* **Pesticide control:** Targeted and minimized pesticide application for environmental protection.
* **Water quality analysis:** Ensuring water suitability for crops.
* **Fertilizer control:** Optimized nutrient delivery based on plant needs.

IoT connectivity plays a crucial role in achieving these goals, leading to cost savings, resource optimization, and reduced human intervention.

### 1.3. Industry 4.0 Aims and Objectives

Agriculture 4.0 represents a significant technological shift, driven by climate change and the need for sustainable practices. It focuses on integrating:

* **Big data analytics:** Deriving insights from large datasets for informed decision-making.
* **Uncrewed aerial surveillance vehicles (UAVs):** Aerial monitoring and data collection for efficient farm management.
* **Internet of Things (IoT):** Connecting devices and systems for real-time data exchange.
* **Artificial intelligence (AI) and machine learning:** Utilizing algorithms for intelligent automation and predictive modeling.

These advancements aim to optimize food supply chains, improve traceability, and enhance overall efficiency in agriculture.

## 2. Challenges of Optimized Environment and Resources Management

### 2.1. Optimized Environment Challenges

#### 2.1.1. Standardization of IoT Platforms

Despite progress, the lack of standardization across IoT platforms poses challenges. Different regions have varying technological capabilities and challenges, resulting in diverse iterations of Agriculture 4.0.

#### 2.1.2. Future Uncertainties

The future of IoT in agriculture is not without uncertainties:

* **Limited uptake:** Despite potential benefits, IoT adoption in farming remains limited due to factors like cost and perceived return on investment.
* **Hype surrounding emerging technologies:** Overly optimistic expectations regarding new technologies can hinder realistic assessments.
* **Inadequate business models:**  Profitable commercialization models for IoT technologies in agriculture need further development.

### 2.2. Resources Management Challenges

#### 2.2.1. Energy Management

IoT offers significant potential for energy savings in greenhouses, but challenges exist:

* **Limited information on cost benefits:** Real-world data on long-term cost savings from energy-saving IoT sensors is scarce.
* **Power supply for electronic equipment:** Providing constant power to a critical mass of sensors remains a challenge.

Solutions for energy conservation include:

* **Low-power communication networks:** Utilizing BLE, ZigBee, NB-IoT, and LoRa for efficient data transmission.
* **Smart sensors:** Optimizing heating/cooling systems and renewable energy sources.
* **Automated temperature regulation:** Utilizing predictive models and algorithms for efficient climate control.

#### 2.2.2. Water Management

IoT contributes to environmental protection by minimizing pesticide use and optimizing water resources. However, challenges persist:

* **Groundwater contamination:** Excessive pesticide use poses risks to groundwater and human health.
* **Sustainable pesticide management:**  Balancing the need for pest control with environmental and health considerations.

#### 2.2.3. E-Waste Management

The widespread adoption of IoT technologies raises concerns about electronic waste generation. However, IoT can also facilitate e-waste management through:

* **IoT-mediated waste collection systems:** Smart waste disposal using sensors and connected devices.
* **Nanomaterial applications:** Utilizing nanomaterials from sensors for pesticide degradation and pollutant detection.

#### 2.2.4. Communication Services Management

Selecting the appropriate communication infrastructure is crucial for efficient IoT deployment in agriculture. Key considerations include:

* **Short-range communication:** BLE offers cost-effective solutions for short distances, but with limitations in data volume.
* **Long-range communication:** LoRaWAN provides extended coverage ideal for open-field agriculture, offering low power consumption and security.
* **Network interoperability:** Enabling seamless communication between different networks and devices is crucial for optimized data exchange.

#### 2.2.5. Structural Integrity and Materials

IoT plays a role in monitoring the structural health of farm buildings:

* **Traditional materials:** Concrete, glass, and plastic are prone to corrosion and environmental degradation.
* **Nanomaterial integration:** CNTs and graphene offer improved structural properties and durability.
* **Structural health monitoring (SHM):** IoT-based systems can monitor the impact of environmental factors on building materials, enhancing resource management.

### 2.3. Problems, Solutions, and Challenges

#### 2.3.1. Network Interoperability Solutions

* **Uneven distribution of IoT infrastructure:** Advanced economies dominate in IoT adoption, highlighting the need for broader access in developing nations.
* **Standardization efforts:** Collaboration between organizations like ETSI, IEEE, and ITU is crucial for establishing interoperable IoT infrastructure.

## 3. IoT Protocols and Architectures for Greenhouses

### 3.1. IoT Protocols

Various protocols exist, each with specific applications:

* **MQTT:**  Efficient protocol for low-bandwidth communication, gradually replacing HTTP.
* **DDS:**  Facilitates low-latency messaging, particularly beneficial for inter-agent communication in smart grids.
* **ZigBee:**  Suitable for low-duty cycle applications, widely used in irrigation, pest control, and water quality analysis.
* **Cloud computing:**  Low-cost and energy-efficient system for data storage and analysis.

### 3.2. Existing Approaches in IoT Architectures

* **Cyber-physical systems (CPS):** Integrating physical processes with computational capabilities for enhanced automation and decision-making.
* **Edge computing:** Processing data closer to the source, reducing latency and bandwidth requirements.

### 3.3. Market Maturity Challenges

* **High cost of sensors:**  Accurate and multifunctional sensors for agriculture remain expensive, hindering widespread adoption, especially among smallholder farmers.
* **Uneven distribution of network infrastructure:**  Limited access to 4G/5G and GPS in rural areas restricts IoT implementation.

### 3.4. Challenges in the Context of Industry 4.0

* **Developing affordable sensors:** R&D efforts are crucial for reducing sensor costs and improving functionalities.
* **Addressing socio-economic factors:** Factors such as risk aversion, demographics, and access to credit influence IoT adoption among farmers.

## 4. Digital Transformation: Towards Greenhouse 4.0

### 4.1. Industry 4.0 Core Technologies

Key technologies driving the digital transformation in agriculture:

* **Wireless sensor networks (WSN):**  Distributed networks of sensors for data collection and monitoring.
* **Machine-to-machine (M2M) communication:**  Enabling direct data exchange between devices.
* **LoRaWAN:** Long-range, low-power protocol ideal for open-field agriculture.
* **RFID systems:**  Tracking and tracing agricultural products.
* **Digital twins:** Virtual representations of physical assets for real-time monitoring and analysis.

### 4.2. Artificial Intelligence and Edge Computing

* **AI in safety management:**  Enhancing fire detection and hazard mitigation through intelligent systems.
* **Edge computing in smart agriculture:**  Processing data locally for faster response times and reduced dependence on cloud infrastructure.

### 4.4. The Overall Merit for Commercial Greenhouses

IoT offers various advantages for commercial greenhouses:

* **CO2 enrichment:**  Optimizing CO2 levels for enhanced photosynthesis and crop yields.
* **Precise agrochemical application:**  Minimizing pesticide use and reducing environmental impact.
* **Microclimate regulation:**  Maintaining optimal temperature, humidity, and light intensity for improved crop growth.

While initial investments in IoT infrastructure can be high, the long-term benefits, including energy and water savings, improved yields, and reduced environmental impact, outweigh the costs, making it a sustainable solution for modern agriculture.

## 5. Conclusion

IoT technologies offer significant potential for optimizing greenhouse environments and resource management in agriculture. Overcoming challenges related to standardization, cost, and infrastructure availability will be crucial for unlocking the full benefits of Agriculture 4.0 and achieving sustainable and efficient food production systems.
"""

result = crew.kickoff(inputs={"gemini": gemini_output})

print(result)

with open("output.md", "w") as f:
    f.write(result)
