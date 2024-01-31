Feature: Testing content pages
  Background:
    Given User can enter to the https://www.canvas8.com/login
    And User can login
    Then Verify Home link is present

  Scenario Outline: Test content page is loading perfectly with given given content page link
    Given User can enter to the <website>
    Then User can see the content related to the subject

   Examples:
    | website|
    | https://www.canvas8.com/library/signals/2023/11/22/the-unseen-machine-sparks-debate-on-ai-in-creativity|
    | https://www.canvas8.com/library/signals/2023/11/20/doves-short-film-disrupts-anxiety-around-ageing|
    | https://www.canvas8.com/library/signals/2023/11/14/dior-launches-luxury-fragrance-line-for-babies|
