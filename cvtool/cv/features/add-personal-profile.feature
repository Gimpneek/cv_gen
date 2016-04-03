Feature: Add personal profile
  As A Job Hunter
  In Order for potential employers to contact me and know who I am
  I Want to include contact details, a personal statement and links to my work

  Scenario: Add name
    When I add a new personal profile
    Then I should be able to add my name

  Scenario: Add email address
    When I add a new personal profile
    Then I should be able to add my email address

  Scenario: Add website
    When I add a new personal profile
    Then I should be able to add a link to my website

  Scenario: Add portfolio
    When I add a new personal profile
    Then I should be able to add a link to my portfolio

  Scenario: Add personal statement
    When I add a new personal profile
    Then I should be able to add a paragraph that describes me

  Scenario: Add minimal information for personal profile
    When I add a new personal profile
    Then I should be able to submit the form by only adding:
      | information        |
      | name               |
      | email address      |
      | personal statement |