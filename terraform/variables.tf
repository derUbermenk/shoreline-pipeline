variable "allowed_ingress_ips" {
  type    = list(string)
}

variable "dev_resource_environment" {
  type    = string
  default = "Shoreline-Dev"
}
