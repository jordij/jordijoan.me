# -*- mode: ruby -*-
# vi: set ft=ruby :

# Set your project name
PROJECT_NAME = 'jordinz'
 
Vagrant.configure(2) do |config|
    # Base box to build off, and download URL for when it doesn't exist on the user's system already
    config.vm.box = "torchbox/wagtail"
    config.vm.box_version = "~> 1.0"

    # Forward a port from the guest to the host, which allows for outside
    # computers to access the VM, whereas host only networking does not.
    config.vm.network "forwarded_port", guest: 8000, host: 8111
    config.vm.network "forwarded_port", guest: 5432, host: 15432

    # Share additional folders, one with the project, another with the media folder mounted from
    # the preview site in delila
    config.vm.synced_folder ".", "/home/vagrant/" + PROJECT_NAME
    
    # Export var
    config.vm.provision "shell",
        inline: "export VAGRANT_PREFER_SYSTEM_BIN=1"

    # Forward agent
    config.ssh.forward_agent = true

    # Enable provisioning with a shell script.
    config.vm.provision :shell, :path => "vagrant/postgres.sh"
    config.vm.provision :shell, :path => "vagrant/provision.sh", :args => [PROJECT_NAME, "requirements/dev.txt"]

    # If a 'Vagrantfile.local' file exists, import any configuration settings
    # defined there into here. Vagrantfile.local is ignored in version control,
    # so this can be used to add configuration specific to this computer.
    if File.exist? "Vagrantfile.local"
        instance_eval File.read("Vagrantfile.local"), "Vagrantfile.local"
    end
end
