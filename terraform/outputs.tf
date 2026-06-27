output "instance_public_ip" {
  description = "Javni IP EC2 instance"
  value       = aws_instance.k3s_node.public_ip
}

output "ssh_command" {
  description = "Komanda za SSH konekciju na instancu"
  value       = "ssh -i ~/.ssh/healthcare-crm-key ubuntu@${aws_instance.k3s_node.public_ip}"
}
