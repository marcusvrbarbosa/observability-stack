terraform {
  backend "s3" {
    bucket = "projeto-stack-obs-tf"  # Crie um bucket S3 com este nome
    key    = "terraform.tfstate"
    region = "sa-east-1"
  }
}