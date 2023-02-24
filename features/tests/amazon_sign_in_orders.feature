# Created by anavisekruna at 2/23/23
Feature: Amazon sign in
  logged out user sees Sign In when clicking on Returns and Orders

 #HW 3 task 2
  Scenario: Logged out user sees Sign In when clicking on Returns and Orders
    Given Open Amazon page
    When Click on Returns & Orders
    Then Verify that Sign in page opened

 #HW 3 task 3
  Scenario: User can click on cart icon and verify that cart is empty
    Given Open Amazon page
    When Click on cart icon
    Then Verify that you see your cart is empty message

#HW 3 task 4
 Scenario: User can add a product to the cart
   Given Open Amazon page
   When Input book
   When Click on search button
   When Click on the first product
   When Click on add to cart button
   When Click on cart icon
   Then Verify that cart has 1 item

