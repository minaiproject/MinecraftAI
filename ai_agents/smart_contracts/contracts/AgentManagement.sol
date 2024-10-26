// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AgentManagement {
    mapping(address => bool) public hasAccess;

    function grantAccess(address _user) external {
        hasAccess[_user] = true;
    }

    function revokeAccess(address _user) external {
        hasAccess[_user] = false;
    }

    function checkAccess(address _user) external view returns (bool) {
        return hasAccess[_user];
    }
}
