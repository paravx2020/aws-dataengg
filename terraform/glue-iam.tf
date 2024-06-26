resource "aws_iam_role" "glue" {
  name = "${var.name_prefix}-${var.service}-AWSGlueServiceRoleDefault"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "glue.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "glue" {
    role = "${aws_iam_role.glue.id}"
    policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
}

resource "aws_iam_role_policy" "my_s3_policy" {
  name = "${var.name_prefix}-${var.service}-s3-policy"
  role = "${aws_iam_role.glue.id}"
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:*"
      ],
      "Resource": [
        "arn:aws:s3:::${var.name_prefix}-${var.service}-bucket",
        "arn:aws:s3:::${var.name_prefix}-${var.service}-bucket/*"
      ]
    }
  ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "glue1" {
  role       = aws_iam_role.glue.id
  policy_arn = "arn:aws:iam::aws:policy/AWSGlueConsoleFullAccess"
}

# ## example for adding multiple aws managed permissions
# ## 1. AWSLambdaBasicExecutionRole
# ## 2. AmazonSageMakerFullAccess
# resource "aws_iam_role_policy_attachment" "lambda" {
#   for_each = toset([
#     "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole", 
#     "arn:aws:iam::aws:policy/AmazonSageMakerFullAccess"
#   ])

#   role       = aws_iam_role.lambda.name
#   policy_arn = each.value
# }
