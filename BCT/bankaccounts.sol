// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {
    uint public balance; // stores balance of the account
    address public accountOwner; // owner of this account

    // Constructor: sets the owner when contract is deployed
    constructor() {
        accountOwner = msg.sender;
    }

    // Deposit Ether into the account
    function deposit() public payable {
        require(msg.sender == accountOwner, "Only owner can deposit");
        require(msg.value > 0, "Deposit must be greater than 0");
        balance += msg.value;
    }

    // Withdraw Ether from the account
    function withdraw(uint amount) public {
        require(msg.sender == accountOwner, "Only owner can withdraw");
        require(amount > 0, "Withdraw must be greater than 0");
        require(balance >= amount, "Insufficient balance");
        balance -= amount;
        payable(accountOwner).transfer(amount);
    }

    // Show current account balance
    function showBalance() public view returns (uint) {
        return balance;
    }
}
