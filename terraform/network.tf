# VPC - izolovana virtuelna mreza za nase resurse
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "${var.project_name}-vpc"
  }
}

# Javni subnet - EC2 instanca ovde dobija javni IP
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block               = "10.0.1.0/24"
  availability_zone        = "${var.aws_region}a"
  map_public_ip_on_launch  = true

  tags = {
    Name = "${var.project_name}-public-subnet"
  }
}

# Internet Gateway - vrata izmedju VPC-a i interneta
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "${var.project_name}-igw"
  }
}

# Route table - kaze "sav saobracaj koji ne ide unutar VPC-a, ide na internet"
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = {
    Name = "${var.project_name}-public-rt"
  }
}

# Povezivanje subneta sa route table-om
resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

# Security Group - firewall pravila za EC2 instancu
resource "aws_security_group" "ec2" {
  name        = "${var.project_name}-ec2-sg"
  description = "Dozvoljava SSH (samo moj IP), HTTP, HTTPS i k3s API port"
  vpc_id      = aws_vpc.main.id

  ingress {
    description = "SSH - samo sa mog IP-a"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.my_ip]
  }

  ingress {
    description = "HTTP - za nas FastAPI backend"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTPS - za kasnije ako dodamo SSL"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Sav izlazni saobracaj dozvoljen"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.project_name}-ec2-sg"
  }
}
