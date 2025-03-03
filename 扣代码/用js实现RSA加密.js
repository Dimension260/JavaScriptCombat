var JSEncrypt = require('node-jsencrypt')
// encrypt.js

function encryptMessage(msg) {
  const encryptor = new JSEncrypt();
  encryptor.setPublicKey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDA5Zq6ZdH/RMSvC8WKhp5gj6Ue4Lqjo0Q2PnyGbSkTlYku0HtVzbh3S9F9oHbxeO55E8tEEQ5wj/+52VMLavcuwkDypG66N6c1z0Fo2HgxV3e0tqt1wyNtmbwg7ruIYmFM+dErIpTiLRDvOy+0vgPcBVDfSUHwUSgUtIkyC47UNQIDAQAB");
  return encryptor.encrypt(msg);
}

// 导出函数供 PyExecJS 调用
module.exports = { encryptMessage };