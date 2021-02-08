## An Introduction to Chef
### What is Chef?  

- A way to use code to fix physical hardware environments.
- Using scripts called recipes chef will make sure every system automatically sets itself to the correct system state if a failure occurs. 
- Automation tool that converts infrastructure to code
- Gives the ability to manage multiple systems with ease
- A Cookbook lives on the server  

### Components of Chef

#### Workstation 

- A recipe is located on a workstation which consists of configurations written in Ruby.  
- A knife is a CLI tool that is used to communicate between recipes and the server

#### Server

- A Cookbook is a collection of recipes 

#### Node

- **Ohai** fetches the current state of the nodes
- **Chef client** configures the nodes based on what is in the Cookbook


## Installing Chef Infra Server and Chef Workstation 

This is a resource for documenting my experience installing Chef Infra Server and Chef Workstation. I followed the below list of links for instruction: 

- [Install Chef Server](https://docs.chef.io/server/install_server/ "Install Chef Server")  

- [Install Work Station](https://docs.chef.io/workstation/install_workstation/)

- [Additional Resource for Installation](https://www.linode.com/docs/guides/install-a-chef-server-workstation-on-ubuntu-18-04/#install-the-chef-server)


## Environment Setup 


