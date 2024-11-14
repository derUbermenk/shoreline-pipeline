variable "allowed_ingress_ips" {
  type    = list(string)
  default = [ "175.176.66.194/32" ]
}

variable "dev_resource_environment" {
  type    = string
  default = "Shoreline-Dev"
}
