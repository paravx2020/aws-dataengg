module "s3_bucket" {
  source = "terraform-aws-modules/s3-bucket/aws"

  bucket = "${var.name_prefix}-${var.service}-bucket"
  #acl    = "private"

  control_object_ownership = true
  object_ownership         = "BucketOwnerEnforced"

#   versioning = {
#     enabled = true
#   }
}

## setup lifecycle config for the bucket

