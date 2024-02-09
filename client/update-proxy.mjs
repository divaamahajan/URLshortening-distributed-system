import fs from 'fs/promises';
import os from 'os';

(async () => {
  const interfaces = os.networkInterfaces();
  let ipAddress = null;
  Object.values(interfaces).forEach((netInterfaces) => {
    netInterfaces.forEach((interfaceInfo) => {
      if (interfaceInfo.family === 'IPv4' && !interfaceInfo.internal) {
        ipAddress = interfaceInfo.address;
      }
    });
  });

  if (ipAddress) {
    try {
      const packageJsonString = await fs.readFile('./package.json', 'utf-8');
      const packageJson = JSON.parse(packageJsonString);
      packageJson.proxy = `http://${ipAddress}:8000`;
      await fs.writeFile('./package.json', JSON.stringify(packageJson, null, 2));
      console.log('Proxy updated to:', packageJson.proxy);
    } catch (error) {
      console.error('Error updating proxy:', error);
    }
  } else {
    console.error('Failed to retrieve internal IP address.');
  }
})();
