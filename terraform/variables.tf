variable "allowed_ingress_ips" {
  type    = list(string)
  default = [ "103.104.17.0/32" ]
}

variable "dev_resource_environment" {
  type    = string
  default = "Shoreline-Dev"
}
