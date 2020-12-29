# Design

Store UI preferences

## Accounts

Probably don't need to filter accounts - unlikely to be that many?

- 

## Transactions

- List of transactions by:
    - 1-* accounts
    - From transaction date
    - To transaction date
    - Category  
    - Content search (description/comment?)
- Display configurable transaction properties
- Allow multi-row selection to assign category or edit comment
- Allow manual adding or deletion of transactions. (Deleted transactions remain in database.)
- Allow pagination of results

## Statements

- Allow statements to be uploaded to server for review (display on screen for confirmation)

## Categories

These become 'virtual accounts' - each being a 'pot' of money - which in turn can be: budgets/categories/savings.

These will require 'virtual transactions' to transfer money between categories.

All transfers should show source/destination account.