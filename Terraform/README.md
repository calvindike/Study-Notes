### Terraform Learning and Practice Repository

<details>
<summary> Install Terraform on MacOS and turn on autocomplete for zsh </summary>

$ `brew tap hashicorp/tap`  
$ `brew install hashicorp/tap/terraform`  
$ `terraform -install-autocomplete`  
$ `exec zsh`  

</details>

<details>
<summary> Install Terraform on Ubuntu and turn on autocomplete for bash </summary>

$ `wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg`  
$ `echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list`  
$ `sudo apt update && sudo apt install terraform`  
$ `terraform -install-autocomplete`  
$ `exec bash`  

</details>
