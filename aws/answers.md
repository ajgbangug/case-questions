# AWS Questions

## 1 - AWS Security: Enterprise Application Suite

Setting the default encryption on the S3 bucket itself would seem to be the solution that would need the least configuration. The KMS key can also be assigned on the bucket level.

## 2 - AWS Web APP: Handling DOS Traﬃc

AWS WAF has a feature called Bot Control that has some built-in rules for managing use cases for bots and crawlers. While I have not personally used this feature, I have used the base AWS WAF in the past for adding some rate-limiting and using some of its built-in rules to add some security to load balancers that can be accessed via the internet.

## 3 - Application Load Balancer

If the two functions are located in the same region, Function B hitting the concurrency limits can affect Function A's ability to process requests. It would be good idea to investigate the reason why function B is hitting the concurrency limits. This is to determine whether the cause of the concurrency issue is interal (such as a misconfiguration) or external (such as a denial-of-service attack).

As for Function A, it would also be good to check for any misconfiguration such as missing Invoke permissions to the ALB for the function.

## 4 - Developer Associate

* A role needs to be created in Account B that the function in Account A can assume as.
* A role on Account A that has policies that allow it to assume previously mention role on Account B should also be created. This role should be attached to the function that will do the cross-account access.
* The role in Account B needs to have the appropriate permissions for the type of access that the lambda function in Account A needs.
* It would be good to check if the cross-account access would be on the same region so as to avoid unintended latency.
