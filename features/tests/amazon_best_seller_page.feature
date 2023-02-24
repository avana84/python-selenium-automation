# Created by anavisekruna at 2/23/23
Feature: Amazon best seller page tests
   Scenario: Verify that there are 5 links on the Amazon Best-Sellers page
    Given Open Amazon best sellers page
    Then Verify that header has 5 links