# Created by asorokin at 4/24/23
Feature: User is able to add a product to cart

  Scenario: User adding a product to cart
    Given Open Cureskin
    When Open Product Details page
    Then Add product to cart
    And Click View cart
    And Verify user is taken to the cart page