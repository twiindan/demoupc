Feature: Geoencoding
    As a user
    I want enter to gmail application when I introduce my username and password
    in order to obtain my emails

    Scenario Outline: Introduce a incorrect login and password
        Given a user registered with username "qafiber" and password "testingfiber"
        When I enter <username> and <password>
        Then I obtain an <error>

        Examples:
            |   username        |   password        |
            |   qafiber         |   qafiber         |
            |   testingfiber    |   testingfiber    |
            |   hello           |   bye             |
            |   qafiber         |                   |
            |                   |   testingfiber    |



    Scenario Outline: Introduce a correct login and password
        Given a user registered with username "qafiber" and password "testingfiber"
        When I enter <username> and <password>
        Then I enter to my account

        Examples:
            |   username    |   password        |
            |   qafiber     |   testingfiber    |