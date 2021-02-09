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

- A Cookbook (a collection of recipes) is located on the server.  

#### Node

- **Ohai** fetches the current state of the nodes
- **Chef client** configures the nodes based on what is in the Cookbook


## Installing Chef Infra Server and Chef Workstation 

This is a resource for documenting my experience installing Chef Infra Server and Chef Workstation. I followed the below list of links for instruction: 

- [Install Chef Server](https://docs.chef.io/server/install_server/ "Install Chef Server")  

- [Install Work Station](https://docs.chef.io/workstation/install_workstation/)

- [Additional Resource for Installation](https://www.linode.com/docs/guides/install-a-chef-server-workstation-on-ubuntu-18-04/#install-the-chef-server)
- [Video Instructions](https://www.youtube.com/watch?v=gOw2Ot2uB1Q&ab_channel=HowToMakeTechWork)


## Environment Setup 
2 VMs both running Kali Linux

`kali-chef-server`

### Ubuntu Setup for Chef Infra Server

1. Download the package for Ubuntu `wget https://packages.chef.io/files/stable/chef-server/14.0.65/ubuntu/20.04/chef-server-core_14.0.65-1_amd64.deb` and then `sudo dpkg -i /tmp/chef-server-core_14.0.65-1_amd64.deb`
2. After a few minutes run `sudo chef-server-ctl reconfigure`
3. Make a new directory by running `mkdir ~/.chef`
4. Run the following command to create an administrator `sudo chef-server-ctl user-create USER_NAME FIRST_NAME LAST_NAME EMAIL 'PASSWORD' --filename FILE_NAME` **Example**:  



`kali-chef-client` 

- Chef Workstation
