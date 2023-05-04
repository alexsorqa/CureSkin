# Created by asorokin at 4/25/23
Feature: Verify cart functionality

  Scenario: Cart functionality verification
    Given Open Cureskin
    When Open Product Details page
    Then Add product to the cart
    And Click View cart
    And Verify a product name and price in cart