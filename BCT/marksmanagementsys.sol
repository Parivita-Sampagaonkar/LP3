// SPDX-License-Identifier: UNLICENSED
pragma solidity >=0.7.0 <0.9.0;

contract MarksManagmtSys {
    struct StudentStruct {
        uint ID;
        string fName;
        string lName;
        uint marks;
    }

    address public owner;
    uint public stdCount = 0;
    StudentStruct[] public stdRecords;

    constructor() {
        owner = msg.sender;
    }

    function addNewRecords(
        uint _ID,
        string memory _fName,
        string memory _lName,
        uint _marks
    ) public {
        stdCount++;
        stdRecords.push(StudentStruct(_ID, _fName, _lName, _marks));
    }

    function getAllRecords() public view returns (StudentStruct[] memory) {
        StudentStruct[] memory records = new StudentStruct[](stdRecords.length);
        for (uint i = 0; i < stdRecords.length; i++) {
            records[i] = stdRecords[i];
        }
        return records;
    }

    // fallback function to handle calls to non-existing functions
    fallback() external payable {
        // Called when no function matches
    }

    // receive function to handle plain ETH transfers
    receive() external payable {
        // Accept ETH transfers
    }
}
