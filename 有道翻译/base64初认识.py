import base64
import binascii

# s = '吴迪简单'.encode('utf-8')
# print(s)
# bs = b'\xe5\x90\xb4\xe8\xbf\xaa\xe7\xae\x80\xe5\x8d\x95'
# bs1 = base64.b64encode(bs)
# print(bs1)
# bs1 = b'5ZC06L+q566A5Y2V'
# bs2 = base64.b64decode(bs1)
# print(bs2)

# s = "Z21kD9ZK1ke6ugku2ccWu-MeDWh3z252xRTQv-wZ6jddVo3tJLe7gIXz4PyxGl73nSfLAADyElSjjvrYdCvEP4pfohVVEX1DxoI0yhm36ytQNvu-WLU94qULZQ72aml6cYBVU_O5b4O-ND0rEWbfEEp-CNsPQEwjRV-iM008hyg4psnuxT9hhBXjpzH8uzBxqR9VBh9v2T35qVb4ipPvX70IaGcbG17rvXyras-RWT24bdytS47IgDmQVMfd1cQrTyDVZo1ByopBhc63S3QOKtcY7Aip1m9eLirsRpmecA4zC-0 Pn2FSpsOJi3Gw6g2Cy8ryt-pnNGsoO2wf_9lWV4Y7LHqAeQfAMcFERawC1PVDQzouFE2Xvyw20H4XCtJMvcdMgnQgmpo42vaU4Uj6SbNLQbWjrCEXEtcrKu9AVGU03oJeo_Stun9oboBASa5gzP7pecQ8NPIB9xciY5O_jk_QuNG-vZVRdTecK1qSEHMpuSgM5dRMN9iTCD93qAwQYE5qOMCuOfeNnWhUewho3XJfMewpsDstvjSesdXfR5rtrrydSw76xvqQotdSH7J0RAUGjj5Wv-WVxelEFbDYQpPvOWHg3wXOa1pORzELoEG6v8_WR5_5C-buAoAC4d9xa1O76dd1nj1e_NzvdicnBPNj0HSt_APXvtqDzmBLEZUwa9b5_ZhgyJldGwdWHzLwxx8xPM34M_YlW28J8msT5RBMgPv9ahAJSsKQReQD4pboP2cwxWC9yPeloFc68TOLIeSrMvXrT8aJw8S5MpAX0C3-2 yN8g0RY80n9QjzsnHIgwXERlrw66hMOHch4DIp-AvbPZl9WTncFPL_A2x-Y4EVkUtvV_JNzDJsVgoITdkekhKHkFmAyMwvKbYvW9-4 pFisyOozkh83rko35YZSqDvvIXEWZyWVpGld2SI_xESEP82gtzgrplZzUuVq_WVDegypnD5DZmZsidnHkau-j5FSYwpivm-96 QgVDIBuYTjvV9Lv9GatSYyZBCjjx0Xi8I-JuH3x12GITyiXmmn5xjbvpLQSBVly_urZpNy1SnH2XCVrZOOauAy_ZgAByrlGlhzxBuGL_fBd2r6Lv4kERgaD6tnGVlBk2inBiPbW8Sex90bE7g0T5ps6w4_jzVmcmQZ-M2cX7u1y7mlV_vF-puzU81na5nvQIaJmWQn0_9-466 JGALXEaW7CHb-BqNZTCdLYJgj6n-DbX9sZs8raeEeJsE3aK1P4YmnUgn6wQHQCYLKmDzTC79KoL-6 eCpHe2VD-P48bDfCKLOrqSeLYiWKnZyTAq42h-f9zZtd-fapb4sHO8O0IUF_6DBQ987P9-dvJhghTj8_UIpMjFqBrGDJbnhbGy5Yjn_G1uUtT1usUGwFoBuEJ96r_VPKlxXYjqrgaW3w3ElKr2pEfkKhTKDSLL_inlWGYhTogPsRX8kJubNsZ5V9FcmU2tlGFh5dlDwA-fTTQunsrLt_G40RrK0iWqSvyEjMZi7DqzdeITNK_sk1OlYMguTK6z12P4tzKgV3Ynq6Xo9ToRQE_g9oSH1OEo8mUw7AQ8dNi7FxXjpAJHbfdbKwIjAqUeOfCUJ3UVBMGGR5Um4w80nDvf-gLaxdCePHELy_ev8E-s3K5kADoaE9iFcM5Kz8N_4bfZ_trx6-LufqiDUcT4rNKa42o3pEOUeS9m61MLyRLp2O1YwxypYPNUbl8yK8Q_gTBrTQK3bfo3hs0vDYTpIL1CBLjMNTfip6nv_mE7mZzhOweBpGyoYl1k3kOPSc_0fviR0jdaeYPsaHx-R1V1erV0okwp8kexYr_5FqyFXEnJxGATUoCY5Tc6OfgOh7grXUnVhf2aTG6Uc1ODQk2_h0DkxlFcwUXJf45N3LadYQDs6nN10tiyh6yTL5aZADP1JGgAFAWpXW4GFzIWf4DmjQ3VQKhulLeUEFHOuJgUmzWQtrV831E4EYBVhWAH5050MrhsPbcd1tvYDnvdEOmSi-pUmu7MWoxK95rzfo71bgUHdEbFN3IDSVbYtUYYwegifnjFS17dcyP2q6HTIygor00eEarvj32vWH7TENiqonqGLOuWYcLeRtjRtblY6MAlDvSSxEDeg4cO5PD-MtsgIMvUnGxYUafUp8uAKR1E4LKwA9VLYM5Bl5RMVDLtYyqsUn5zBOZU"
# bs = base64.b64decode(s,b'-_')
# print(bs)

bs = '我喜欢我自己'.encode('utf-8')
# print(bs)
im16 = binascii.b2a_hex(bs)
# print(im16)

result = str(im16)[2:].replace("'","")

ressult2 = binascii.a2b_hex(result)
print(ressult2)