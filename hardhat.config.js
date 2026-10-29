require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  paths: {
    tests: "tests",
  },
  solidity: {
    version: "0.8.24",
    settings: {
      optimizer: {
        enabled: true,
        runs: 200,
      },
      viaIR: true,
      evmVersion: "cancun",
    },
  },
  networks: {
    hardhat: {
      chainId: 31337,
    },
    localhost: {
      url: "http://127.0.0.1:8545",
      chainId: 31337,
    },
    ...(process.env.TESTNET_RPC && process.env.DEPLOYER_KEY ? {
      testnet: {
        url: process.env.TESTNET_RPC,
        accounts: [process.env.DEPLOYER_KEY],
        chainId: parseInt(process.env.TESTNET_CHAIN_ID || "11155111"),
      }
    } : {}),
  },
  gasReporter: {
    enabled: process.env.REPORT_GAS === "true",
    currency: "USD",
    showTimeSpent: true,
  },
};
