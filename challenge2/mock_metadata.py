mock_metadata = {'ami-id': 'ami-0a887e401f7654935', 'ami-launch-index': '0', 'ami-manifest-path': '(unknown)', 'block-device-mapping/ami': '/dev/xvda', 'block-device-mapping/ebs0': 'sdb', 'block-device-mapping/ephemeral0': 'sdb', 'block-device-mapping/root': '/dev/xvda', 'block-device-mapping/swap': 'sdcs', 'elastic-inference/associations': 'eia-bfa21c7904f64a82a21b9f4540169ce1', 'elastic-inference/associations/eia-bfa21c7904f64a82a21b9f4540169ce1': {'version_2018_04_12': {'elastic-inference-accelerator-id': 'eia-bfa21c7904f64a82a21b9f4540169ce1', 'elastic-inference-accelerator-type': 'eia1.medium'}}, 'events/maintenance/scheduled': ['[', '\t{', '\t\t"Code": "system-reboot",', '\t\t"Description": "The instance is scheduled for system-reboot",', '\t\t"State": "active",', '\t\t"EventId": "instance-event-1234567890abcdef0",', '\t\t"NotBefore": "2 Jul 2021 16:16:49 GMT",', '\t\t"NotAfter": "9 Jul 2021 16:16:49 GMT",', '\t\t"NotBeforeDeadline": "11 Jul 2021 16:16:49 GMT"', '\t}', ']'], 'events/recommendations/rebalance': {'noticeTime': '2021-07-02T19:42:58Z'}, 'hostname': 'ip-172-16-34-43.ec2.internal', 'iam/info': {'Code': 'Success', 'LastUpdated': '2020-04-02T18:50:40Z', 'InstanceProfileArn': 'arn:aws:iam::896453262835:instance-profile/baskinc-role', 'InstanceProfileId': 'AIPA5BOGHHXZELSK34VU4'}, 'iam/security-credentials': 'baskinc-role', 'iam/security-credentials/baskinc-role': {'Code': 'Success', 'LastUpdated': '2020-04-02T18:50:40Z', 'Type': 'AWS-HMAC', 'AccessKeyId': '12345678901', 'SecretAccessKey': 'v/12345678901', 'Token': 'TEST92test48TEST+y6RpoTEST92test48TEST/8oWVAiBqTEsT5Ky7ty2tEStxC1T==', 'Expiration': '2020-04-02T00:49:51Z'}, 'instance-action': 'none', 'instance-id': 'i-1234567890abcdef0', 'instance-life-cycle': 'on-demand', 'instance-type': 'm4.xlarge', 'kernel-id': 'aki-5c21674b', 'latest': ['latest', 'api/token'], 'latest/api/token': 'latest/api/token', 'local-hostname': 'ip-172-16-34-43.ec2.internal', 'local-ipv4': '172.16.34.43', 'mac': '0e:49:61:0f:c3:11', 'network/interfaces/macs/0e:49:61:0f:c3:11/device-number': '0', 'network/interfaces/macs/0e:49:61:0f:c3:11/interface-id': 'eni-0f95d3625f5c521cc', 'network/interfaces/macs/0e:49:61:0f:c3:11/ipv4-associations/192.0.2.54': '192.0.2.54', 'network/interfaces/macs/0e:49:61:0f:c3:11/ipv6s': '2001:db8:8:4::2', 'network/interfaces/macs/0e:49:61:0f:c3:11/local-hostname': 'ip-172-16-34-43.ec2.internal', 'network/interfaces/macs/0e:49:61:0f:c3:11/local-ipv4s': '172.16.34.43', 'network/interfaces/macs/0e:49:61:0f:c3:11/mac': '0e:49:61:0f:c3:11', 'network/interfaces/macs/0e:49:61:0f:c3:11/network-card-index': '0', 'network/interfaces/macs/0e:49:61:0f:c3:11/owner-id': '515336597381', 'network/interfaces/macs/0e:49:61:0f:c3:11/public-hostname': 'ec2-192-0-2-54.compute-1.amazonaws.com', 'network/interfaces/macs/0e:49:61:0f:c3:11/public-ipv4s': '192.0.2.54', 'network/interfaces/macs/0e:49:61:0f:c3:11/security-group-ids': 'sg-0b07f8f6cb485d4df', 'network/interfaces/macs/0e:49:61:0f:c3:11/security-groups': 'ura-launch-wizard-harry-1', 'network/interfaces/macs/0e:49:61:0f:c3:11/subnet-id': 'subnet-0ac62554', 'network/interfaces/macs/0e:49:61:0f:c3:11/subnet-ipv4-cidr-block': '192.0.2.0/24', 'network/interfaces/macs/0e:49:61:0f:c3:11/subnet-ipv6-cidr-blocks': '2001:db8::/32', 'network/interfaces/macs/0e:49:61:0f:c3:11/vpc-id': 'vpc-d295a6a7', 'network/interfaces/macs/0e:49:61:0f:c3:11/vpc-ipv4-cidr-block': '192.0.2.0/24', 'network/interfaces/macs/0e:49:61:0f:c3:11/vpc-ipv4-cidr-blocks': '192.0.2.0/24', 'network/interfaces/macs/0e:49:61:0f:c3:11/vpc-ipv6-cidr-blocks': '2001:db8::/32', 'placement/availability-zone': 'us-east-1a', 'placement/availability-zone-id': 'use1-az4', 'placement/group-name': 'a-placement-group', 'placement/host-id': 'h-0da999999f9999fb9', 'placement/partition-number': '1', 'placement/region': 'us-east-1', 'product-codes': '3iplms73etrdhxdepv72l6ywj', 'public-hostname': 'ec2-192-0-2-54.compute-1.amazonaws.com', 'public-ipv4': '192.0.2.54', 'public-keys/0/openssh-key': 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC/JxGByvHDHgQAU+0nRFWdvMPi22OgNUn9ansrI8QN1ZJGxD1ML8DRnJ3Q3zFKqqjGucfNWW0xpVib+ttkIBp8G9P/EOcX9C3FF63O3SnnIUHJsp5faRAZsTJPx0G5HUbvhBvnAcCtSqQgmr02c1l582vAWx48pOmeXXMkl9qe9V/s7K3utmeZkRLo9DqnbsDlg5GWxLC/rWKYaZR66CnMEyZ7yBy3v3abKaGGRovLkHNAgWjSSgmUTI1nT5/S2OLxxuDnsC7+BiABLPaqlIE70SzcWZ0swx68Bo2AY9T9ymGqeAM/1T4yRtg0sPB98TpT7WrY5A3iia2UVtLO/xcTt test', 'ramdisk-id': 'ari-01bb5768', 'reservation-id': 'r-046cb3eca3e201d2f', 'security-groups': 'ura-launch-wizard-harry-1', 'services/domain': 'amazonaws.com', 'services/partition': 'aws', 'spot/instance-action': {'action': 'terminate', 'time': '2021-07-02T19:44:58Z'}, 'spot/termination-time': '2021-07-02T19:44:58Z', '': ['ami-id', 'ami-launch-index', 'ami-manifest-path', 'block-device-mapping/ami', 'block-device-mapping/ebs0', 'block-device-mapping/ephemeral0', 'block-device-mapping/root', 'block-device-mapping/swap', 'elastic-inference/associations', 'elastic-inference/associations/eia-bfa21c7904f64a82a21b9f4540169ce1', 'events/maintenance/scheduled', 'events/recommendations/rebalance', 'hostname', 'iam/info', 'iam/security-credentials', 'iam/security-credentials/baskinc-role', 'instance-action', 'instance-id', 'instance-life-cycle', 'instance-type', 'kernel-id', 'latest', 'latest/api/token', 'local-hostname', 'local-ipv4', 'mac', 'network/interfaces/macs/0e:49:61:0f:c3:11/device-number', 'network/interfaces/macs/0e:49:61:0f:c3:11/interface-id', 'network/interfaces/macs/0e:49:61:0f:c3:11/ipv4-associations/192.0.2.54', 'network/interfaces/macs/0e:49:61:0f:c3:11/ipv6s', 'network/interfaces/macs/0e:49:61:0f:c3:11/local-hostname', 'network/interfaces/macs/0e:49:61:0f:c3:11/local-ipv4s', 'network/interfaces/macs/0e:49:61:0f:c3:11/mac', 'network/interfaces/macs/0e:49:61:0f:c3:11/network-card-index', 'network/interfaces/macs/0e:49:61:0f:c3:11/owner-id', 'network/interfaces/macs/0e:49:61:0f:c3:11/public-hostname', 'network/interfaces/macs/0e:49:61:0f:c3:11/public-ipv4s', 'network/interfaces/macs/0e:49:61:0f:c3:11/security-group-ids', 'network/interfaces/macs/0e:49:61:0f:c3:11/security-groups', 'network/interfaces/macs/0e:49:61:0f:c3:11/subnet-id', 'network/interfaces/macs/0e:49:61:0f:c3:11/subnet-ipv4-cidr-block', 'network/interfaces/macs/0e:49:61:0f:c3:11/subnet-ipv6-cidr-blocks', 'network/interfaces/macs/0e:49:61:0f:c3:11/vpc-id', 'network/interfaces/macs/0e:49:61:0f:c3:11/vpc-ipv4-cidr-block', 'network/interfaces/macs/0e:49:61:0f:c3:11/vpc-ipv4-cidr-blocks', 'network/interfaces/macs/0e:49:61:0f:c3:11/vpc-ipv6-cidr-blocks', 'placement/availability-zone', 'placement/availability-zone-id', 'placement/group-name', 'placement/host-id', 'placement/partition-number', 'placement/region', 'product-codes', 'public-hostname', 'public-ipv4', 'public-keys/0/openssh-key', 'ramdisk-id', 'reservation-id', 'security-groups', 'services/domain', 'services/partition', 'spot/instance-action', 'spot/termination-time', '']}