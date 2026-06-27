variable "aws_region" {
  description = "AWS region gde se podiže infrastruktura"
  type        = string
  default     = "eu-central-1"
}

variable "project_name" {
  description = "Prefiks za imenovanje resursa"
  type        = string
  default     = "healthcare-crm"
}

variable "instance_type" {
  description = "EC2 instance type - MORA biti Free Tier eligible"
  type        = string
  default     = "t3.micro"
}

variable "my_ip" {
  description = "Tvoj javni IP (za SSH pristup) - format x.x.x.x/32"
  type        = string
}
