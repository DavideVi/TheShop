
Vagrant.configure("2") do |config|

  config.vm.box = "archlinux/archlinux"
  config.vm.network "forwarded_port", guest: 8000, host: 80, host_ip: "0.0.0.0", auto_correct: true
  
end
