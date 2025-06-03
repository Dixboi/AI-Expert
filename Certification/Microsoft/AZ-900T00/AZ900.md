# Describe cloud concepts (25–30%)
## Describe cloud computing

### Define cloud computing

Cloud computing: Delivery of computing services over the internet. 

### Describe the shared responsibility model

Consumer
- Information and data stored
- Devices that are allowed to connect
- Accounts and identities of the people, services, and devices

Provider
- Datacenter
- Network
- Hosts

Depends on the model
- Operating systems (*SaaS, PaaS = Provider* | *IaaS = Customer*)
- Network controls (*SaaS = Provider* | *PaaS = Shared* | *IaaS = Customer*)
- Applications (*SaaS = Provider* | *PaaS = Shared* | *IaaS = Customer*)
- Identity and infrastructure (*SaaS, PaaS = Shared* | *IaaS = Customer*)

**SaaS: Software as a Service**

**PaaS: Platform as a Service**

**IaaS: Infrastructure as a Service**

### Define cloud models, including public, private, and hybrid

Private cloud: A dedicated computing environment for a single company. More flexibility but also costs more.

Public cloud: A computing environment where anyone can purchase.

Hybrid cloud: Both private and public.

Multi-cloud: Uses two or more *public* clouds.

#### AZURE TOOLS/SERVICES
1. **Azure Arc**: Set of technologies that helps you to manage your cloud environment.
2. **Azure VMware Solution**: Lets you run your VMware Workloads in Azure.

### Describe the consumption-based model

CapEx: Capital Expenditure. Typically a one-time up-front expense.
OpEx: Operational Expenditure. Spending money overtime based on used resources.

### Compare cloud pricing models

Pay-as-you-go. You pay only on the services that you use. When you're done using cloud resources, you give them back and will not pay until the next usage.

## Describe the benefits of using cloud services
### Describe the benefits of high availability and scalability in the cloud

Availability: Uptime
Scalability: Handling demand

High Availablity: Maximum availability regardless of disruption or events that may occur.

SLA: Service Level Agreement. The agreement between the provider and the customer on how available is the service. If the availability is not met, the provider will provide credits to the customer.

Scalability: Ability to adjust resources to meet demand. If demand is low, resource usage is low. If demand is high, resource usage is high.
- Vertical Scaling: Making the resources more powerful (e.g. more CPUs or RAMs)
- Horizontal Scaling: Adding more resources (e.g. more virtual machines and containers)

### Describe the benefits of reliability and predictability in the cloud

Reliability: Ability of a system to recover from failures and continue to function.

Predictability: predicts the resources needed and the cost
- Performace: Predicting the resources needed
- Cost: Focused on predicting or forecasting the cost of the resources used or needed

### Describe the benefits of security and governance in the cloud

Security: Can pick a cloud solution according to desired control. Well suited to distributed denial of service (DDoS) attacks.

Governance: Has templates to ensure that deployed resources meet corporate standards and government regulatory requirements. Can flag any resources that are out of compliance and provides mitigation strategies. 

### Describe the benefits of manageability in the cloud

Management **of** the cloud: **what** is managing cloud resources
- automatically scale resource deployment
- deploy resources based on preconfigured templates
- monitor health of resources and automatically replace failing ones
- receive automatic alerts based on configured metric

Management **in** the cloud: **how** to manage cloud environment
- web portal
- command line interface (CLI)
- APIs
- PowerShell

## Describe cloud service types
### Describe infrastructure as a service (IaaS)

Infrastructure as a service (IaaS)
- most flexbile because you have the maximum control of your cloud resources
- basically renting hardware

Possible scenarios:
- Lift-and-shift migration: Setting up cloud resources similar to on-premise datacenter. Running from on-premise to IaaS.
- Testing and development: Already have configurations for development and test environments for replicating rapidly. 

### Describe platform as a service (PaaS)

Platform as a Service (PaaS)
- maintains the licensing or patching of operating systems (OSs) and databases
- responsibilities are shared on **network controls**, **applications**, and **identity and directory infrastructure**

Possible scenarios:
- Development framework: Provides a framework for developing or customizing cloud-based application. E.g. Excel Macros
- Analytics or business intelligence: Can mine data for doing analysis or other processes

### Describe software as a service (SaaS)

Software as a Service (SaaS)
- basically renting fully developed application

Possible scenarios:
- Email (MS Outlook)
- Messaging (MS Teams)

# Describe Azure architecture and services (35–40%)
## Describe the core architectural components of Azure
### Describe Azure regions, region pairs, and sovereign regions
Physical infrastructure (datacenter): has resources arranged in racks, power, cooling, and networking

Availability Zone: physically separated datacenters. has at least three separate availability zones connected

Azure Region: contains at least 1 but potentially multiple datacenters

Region pairs: pairs of Azure Regions at least 300 miles away

### Describe Azure resources and resource groups
Resource: basic building block of Azure. Anything created, deployed, etc. Examples are VMs and databases

Resource Group: group of resources. Cannot be nested. A resource is only allowed in ONE group

Azure Subscription: provides access to an account to a resource group

Azure management groups: contains all the Azure subscriptions

## Describe Azure compute and networking services
### Describe Azure Virtual Machine
**Virtual Machines (VMs)**
- IaaS
- can have total control over the OS, run custom software, and use custom host configurations

**Virtual machine scale sets**
- can update a large set of VMs where the VMs are configured the same way and have the same purpose.

**Virtual machine availability sets**
- ensures that VMs have varied power and network connectivity. this prevents to lose VMs in a single power failure

Objectives that availablity accomplishes
1. Update domain: can update a set while the others are running completely fine
2. Fault domain: groups VMs by common power source and network switch to protect against power or networking failure

### Describe Azure virtual desktop
**Azure virtual desktop**
- another type of VM
- desktop and application virtualization device that runs on the cloud

**Enhance security**
- has centralized security for user's desktops with Microsoft Entra ID
- enables multifactor authentication and granular role-based access controls (RBACs) to users
- since the desktop is on the cloud, data and apps are separated from the local hardware

### Describe Azure containers

**Difference between VMs**
- VMs replicate hardware while Containers replicate OS

#### AZURE TOOLS/SERVICES
1. **Azure Container Instances**: fastest and simplest way to run a container in Azure
2. **Azure Container Apps**: similar to Instances but can incorporate load balancing and scaling
3. **Azure Kubernetes Service**: container orchestration service

### Describe Azure functions
#### AZURE TOOLS/SERVICES
1. **Azure Function**
just run the code, no need to setup infrastructure or platform

- stateless (default): behaves as if they restart every time to respond on an event
- stateful (Durable Functions): a context is passed to track prior activity

### Describe application hosting options
1. **Azure App Service**
enables to build and host web apps, background jobs, mobile back-ends, and RESTful APIs. supports Windows and Linux

Can host common app service:
- Web apps
- API apps
- WebJobs
- Mobile apps

### Describe Azure virtual networking
#### AZURE TOOLS/SERVICES
1. **Azure Virtual Networks**: enables Azure resources to communicate with each other, with user on the internet, and with on-premise client computers
2. **Azure ExpressRoute**: provides a dedicated private connectivity to Azure without travelling to the internet
3. **Netwowk Security Groups**: can contain ultiple inbound and output security rules
4. **Network Virtual Appliances**: specialized VMs that carries out a particular network function

Networking Capabilities:
- **Isolation and segmentation**: create isolated virtual networks and define private IP address
- **Internet communications**: enable incoming connection from the internet by assigning a public IP adress
- **Communicate between Azure resources**: can connect Azure resources securely
- **Communicate with on-premises resources**: connect resources to on-premise environment
  - Point-to-site: computer outside to corporate network
  - Site-to-site: on-premise VPN device or gateway to the Azure VPN gateway
  - Azure ExpressRoute
- **Route network traffic**: control default settings in routing through:
  - Route tables
  - Border Gateway Protocol (BGP)
- **Filter network traffic**: filter traffic between subnets through:
  - Network security groups
  - Network virtual appliances
- **Connect virtual networks**: can peer virtual networks

### Describe Azure virtual private networks
#### AZURE TOOLS/SERVICE
1. **Azure VPN Gateway**: deployed in a dedicated subnet of the virtual network

virtual private network (VPN): uses an encrypted tunnel within another network

Methods of authentication:
- Policy-based: evaluates every data packet against sets of IP addresses
- Route-based: decides which tunnel interfaces to use

High-availability scenarios:
a. Active/standby
b. Active/active
c. ExpressRoute failover
d. Zone-redundant gateways

### Describe Azure ExpressRoute
Features and benefits:
1. Connectivity to Microsoft cloud services across all regions in the geopolitical region
2. Global connectivity to Microsoft services across all regions with the ExpressRoute Global Reach
3. Dynamic routing between your network and Microsoft via Border Gateway Protocol (BGP)
4. Built-in redundancy in every peering location for higher reliability

Connectivity models
- CloudExchange colocation
- Point-to-point Ethernet connection
- Any-to-any connection
- Directly from ExpressRoute sites

### Describe Azure DNS
#### AZURE TOOLS/SERVIES:
1. **Azure DNS**: hosting service for DNS domains that provides name resolution by using Microsoft Azure infrastructure

Benefits:
- Reliability and performance
- Security
- Ease of use
- Customizable virtual networks
- Alias records

**NOTE**: Buy first a domain name in App Service then host that domain in Azure DNS

## Describe Azure storage services

### Describe Azure storage accounts
A storage account provides a unique namespace for your Azure Storage data that's accessible from anywhere in the world over HTTP and HTTPS

Redundancy options:
1. Locally redundant storage (LRS)
2. Geo-redundant storage (GRS)
3. Read-access geo-redundant storage (RA-GRS)
4. Zone-redundant storage (ZRS)
5. Geo-zone-redundant storage (GZRS)
6. Read-access geo-zone-redundant storage (RA-GZRS)

### Describe Azure storage redundancy
#### AZURE TOOLS/SERVICE:
1. **Azure Storage**: stores multiple copies of data

Redundancy ensures that your storage account meets its availability and durability targets

**Locally Redundant Storage (LRS)**: replicates data three times within a single data center in the primary region <br>
**Zone-redundant storage (ZRS)**: replicates data synchronously aross three Azure availability zones in the primary region <br>
**Geo-redundant storage (GRS)**: LRS on primary and secondary region <br>
**Geo-zone-redundant storage (GZRS)**: ZRS on primary and LRS on secondary <br>

### Describe Azure storage services
#### AZURE TOOLS/SERVICES:
1. **Azure Blobs**: for text and binary data
2. **Azure Files**: managed file shares for cloud or on-premises deployments
3. **Azure Queues**: messaging service between application components
4. **Azure Disks**: Block-level storage volumes for Azure VMs
5. **Azure Tables**: NoSQL table option for structured, non-relational data

### Identify Azure data migration options 
#### AZURE TOOLS/SERVICES:
1. **Azure Migrate**: helps migrate from on-premises environment to the cloud
2. **Azure Data Box**: physical migration service that helps transfer large amounts of data in quick, inexpensive, and reliable way

### Identify Azure file movement options
#### AZURE TOOLS/SERVICES:
1. **AzCopy**: command-line utility to manage files between accounts
2. **Azure Storage Explorer**: like a GUI of AzCopy
3. **Azure File Sync**: centralize file shares

## Describe Azure identity, access, and security
### Describe Azure directory services
#### AZURE TOOLS/SERVICES:
1. **Microsoft Entra ID**: directory service that enables you to sign in and access both Microsoft cloud applications and cloud application that you develop. For IT administrators, App developers, Users, and Online service subscribers. Provides Authentication, Single sign-on (SSO), Application management, and Device management.
2. **Microsoft Entra Domain Services**: provides managed domain services such as domain join, group policy, lightweight directory access protocol (LDAP), and Kerberos/NTLM authentication.

### Describe Azure authentication models
- Authentication: process of establishing the identity of a person, service, or device. prove WHO they are
- Single sign-on (SSO): sign on ONE TIME and use to access multiple resources and applications from different providers
- Multifactor authentication (MFA): extra form of identification
- passwordless: set up first before it can work, must have something your computer have

#### AZURE TOOLS/SERVICES:
1. **Microsoft Entra multifactor authentication**: provides multifactor authentication capabilities
2. **Windows Hello for Business**: passwordless. designated Windows PC. biometric and PIN credentials are directly tied to the user's PC
3. **Microsoft Authenticator App**: passwordless. can sign-in to any platform or browser by getting a notification on mobile
4. **FIDO2 sescurity keys**: Fast IDentity Online (FIDO). unphishable standards-based passwordless authentication method that can come in any form of factor

### Describe Azure external identities

External identity: a person, device, service that is outside of your organization

Capabilities of Microsoft Entra External ID:
- Business to business (B2B) collaboration: external users use their preferred identity to sign-in to your Microsoft applications
- B2B direct contact: mutual, two-way trust with another Microsoft Entra organization for seamless collaboration
- Microsoft Azure Active Directory business to customer (B2C): publish modern SaaS apps to consumers to customers. uses AZure AD B2C

### Describe Azure conditional access
#### AZURE TOOLS/SERVICES:
1. **Conditional Access**: allow users to access resources based on identity signals such as who the user is, where the user is, and what device the user uses.

### Describe Azure role-based access control
#### AZURE TOOLS/SERVICES:
1. **Azure role-based access control (Azure RBAC): control access

### Describe Zero Trust model
Assumes breach at the outset and then verifies each request as though it originated from an uncontrolled network

Three guiding principles:
1. Verify explicitly: always authenticate and authorize based on all available data points.
2. use least privilege access: limit user access with Just-In-Time and Just-Enough-Access (JIT/JEA), risk-based adaptive policies, and data protection.
3. Assume breach: Minimize blast radius and segment access. Verify end-to-end encryption. Use analytics to get visibility, drive threat detection, and improve defenses.

### Describe defense-in-depth
To protect information and prevent it from being stolen by those who aren't authorized to access it

Seven Layers:
1. Physical security: hardware
2. Identity and access: identities. audit events and changes
3. Perimeter: against network based attacks
4. Network: connectivity
5. Compute: compute resources
6. Application: applications and secrets
7. Data: data storage and data

### Describe Micfrosoft Defender for Cloud
#### AZURE TOOLS/SERVICES:
1. **Microsoft Defender for Cloud**: monitoring tool for security posture management and threat protection

#### AZURE TOOLS/SERVICES:
1. **Microsoft Entra External ID**: refers to ways you can securely interact with users outside of your organization

# Describe Azure management and governance (30–35%)
## Describe cost management in Azure
### Describe factors that can affect costs in Azure

Capital expense (CapEx): building out
Operational expense (OpEx): maintaining

Consumption can be:
- Pay-as-you-go
- Commit: can commit to a set amout of cloud resources and can provide discounts on those reserved resources

#### AZURE TOOLS/SERVICES:
1. **Azure Marketplace**: lets you purchase Azure-based solutions and services from third-party vendors

### Compare the Pricing and Total Cost of Ownership calculators

#### AZURE TOOLS/SERVICES:
1. **Pricing calculator**: for estimating costs for provisioning resources
2. **TCO calculator**: for comparing costs between on-premise and Azure Cloud infrastructure

### Describe the Microsoft Cost Management tool
#### AZURE TOOLS/SERVICES:
1. **Cost Management**: check resources costs, create alerts, create budgets
2. **Cost analysis**: quick visual for Azure costs
3. **Cost alerts**: Notify if the budget is consumed or overconsumed

- Budget alerts: reaches or exceeds on costs
- Credit alerts: Azure credit monetary commitments are consumed
- Department spending quota alerts: when a department spending reaches a fixed threshold of the quota

### Describe the purpose of tags
Tags: to organize resources. provides extra information, or metadata, about your resources

Can be modified using Windows PowerShell, Azure CLI, Azure Resource Manager templates, REST API, or Azure Portal

## Describe features and tools in Azure for governance and compliance
### Describe the purpose of Microsoft Purview
#### AZURE TOOLS/SERVICES:
1. **Microsoft Purview**: data governance, risk, and compliance solutions in a single view

- Risk & compliance: protect sensitive data, identify data risks, manage regulatory compliance
- Unified data governance: data classification, manage access to data, get insights about data

### Describe the purpose of Azure Policy
#### AZURE TOOLS/SERVICES:
1. **Azure Policy**: create, assign, and manage policies to control and audit resources

Azure Policy initiative is a way of grouping related policies together

Policy definitions that are included:
- Monitor unencrypted SQL Database in Security Center: for unencrypted SQL databases and servers
- Monitor OS vulnerabilities in Security Center: for servers that don't satisfy the configured OS vulnerability baseline
- Monitor missing Endpoint Protection in Security Center: for servers that don't have an installed endpoint protection agent

### Describe the purpose sof resource locks
Prevents resources to be accidentally deleted or changed

Types:
- Delete: cannot be deleted but can be modified
- ReadOnly: cannot be deleted and cannot be modified

### Describe the purpose of the Service Trust portal
#### AZURE TOOLS/SERVICES:
1. **Microsoft Service Trust Portal**: provides access to contents and tools about Microsoft security, privacy, and compliance practices

## Describe features and tools for managing and deploying Azure resources
### Describe tools for interacting with Azure
#### AZURE TOOLS/SERVICES:
1. **Azure portal**: web-based GUI for managing Azure subscription
2. **Azure Cloud Shell**: browser-based shell tool to manage Azure resources using shell. Both supports Azure Power Shell and Azure CLI
3. **Azure PowerShell**: uses PowerShell commands
4. **Azure Command Line Interface**: uses Bash commands

### Describe the purpose of Azure Arc
#### AZURE TOOLS/SERVICES:
1. **Azure Arc**: helps in managing hybrid and multi-cloud configurations. allows to manage resources outside of Azure

### Describe Azure Resource Manager and Azure ARM templates
#### AZURE TOOLS/SERVICES:
1. **Azure Management Resources**: aka ARM. Anything you do with Azure Resources involves ARM. Deployment and management service for Azure

## Describe monitoring tools in Azure
### Describe the purpose of Azure Advisor
#### AZURE TOOLS/SERVICES:
1. **Azure Advisor**: evaluates Azure resources and makes recommendations. Designed to help save time on cloud optimization

The recommendations are available in Azure portal and the API. Can also set up notifications for alerts.

Five categories of recommendations:
- Reliability: improve continuity
- Security: detect threats
- Performance: improve speed
- Operational Excellence: efficiency, manageability, and best practices
- Cost: spending

### Describe Azure Service Health
#### AZURE TOOLS/SERVICES:
1. **Azure Service Health**: helps keep track of Azure resource, both your specifically deployed resources and the overall status of Azure
2. **Azure Status**: global view of all Azure services across all regions
3. **Service Health**: provides a narrower view of services. recommended for looking at Azure services and regions that you use
4. **Resources Health**: focuses on individual cloud resources

### Describe Azure Monitor
#### AZURE TOOLS/SERVICES:
1. **Azure Monitor**: platform for collecting data on your resources, visualizing, and can also act on the results
2. **Azure Log Analytics**: write and run log queries
3. **Azure Monitor Alerts**: provides an automated way to stay informed when Azure Monitor detects a threshold being crossed
4. **Application Insights**: Azure Monitor feature. monitors web applications 
