The Treatment Episode Data Set Admissions (TEDS-A), 2023: Public Use File (PUF) Codebook was prepared for the Substance Abuse and Mental Health Services Administration (SAMHSA), under Contract No. 75S20320C00001 with SAMHSA, U.S. Department of Health and Human Services (HHS). Elizabeth Crane served as contracting officer representative.

## Recommended Citation

Substance Abuse and Mental Health Services Administration: Treatment Episode Data Set Admissions (TEDS-A), 2023: Public Use File (PUF) Codebook. Substance Abuse and Mental Health Services Administration, 2025.

## Originating Office

Center for Behavioral Health Statistics and Quality, Substance Abuse and Mental Health Services Administration, 5600 Fishers Lane, Rockville, MD 20857. Released 2025.

## Electronic Access

This codebook may be downloaded from https://www.samhsa.gov/data/data-we-collect/teds- treatment-episode-data-set/datafiles.

## Disclaimer

Nothing in this document constitutes a direct or indirect endorsement by SAMHSA or HHS of any non-federal entity’s products, services, or policies. Stock photos used in this publication are copyrighted and are for illustrative purposes only. Any person depicted in a stock photo is a model.

## Public Domain Notice

This publication is in the public domain and may be reproduced or copied without permission from SAMHSA. Citation of the source is appreciated. However, this publication may not be reproduced or distributed for a fee without the specific, written authorization of the Office of Communications, SAMHSA, HHS.

Released 2025

# TREATMENT EPISODE DATA SET — ADMISSIONS (TEDS-A), 2023

## Introduction to TEDS

The Treatment Episode Data Set (TEDS) system serves as a repository for treatment data routinely collected by states for the purposes of monitoring their substance use treatment systems. It is comprised of selected data items from states’ administrative records that are converted to a standardized format, which is consistent across all states. The TEDS system is comprised of two major components: the Admissions Data Set (TEDS-A) and the Discharges Data Set (TEDS-D). Data for the TEDS-A file were first reported in 1992, while data for the TEDS-D were first reported in 2000.

## Admissions

TEDS-A provides demographic, clinical, and substance use characteristics of persons admitted to substance use treatment services. The unit of analysis is treatment admissions to state-licensed or certified substance use treatment centers that receive federal public funding. TEDS-A has two parts: a minimum data set and a supplemental data set. The former is collected by all states; the latter is collected by some. The minimum data set consists of 19 items that include:

- demographic information;
- primary, secondary, and tertiary substances used by the subject, and their route of administration, frequency of use, and age at first use;
- source of referral to treatment;
- number of prior treatment episodes; and
- service type, including planned use of medication-assisted (i.e., methadone, buprenorphine, or naltrexone) opioid therapy. TEDS-A’s supplemental data set includes 15 psychiatric, social, and economic items.

## Discharges

The second major component of the TEDS system, TEDS-D (consisting of discharge records), includes the same variables as the admissions (TEDS-A) component, with the addition of:

- type of service at discharge,
- length of stay, and
- reason for discharge or discontinuation of service.

## Management of TEDS

Since 1992, the Center for Behavioral Health Statistics and Quality, or CBHSQ (known until 2010 as the Office of Applied Studies, or OAS), of the Substance Abuse and Mental Health Services Administration (SAMHSA), U.S. Department of Health and Human Services (HHS), has funded and been responsible for TEDS. CBHSQ coordinates and manages the collection of TEDS data from the 50 U.S. states, the District of Columbia, and U.S. territories.

CBHSQ also develops descriptive and analytical reports from TEDS to provide national- and state-level data on the number and types of clients treated, as well as the characteristics of facilities providing services.

## Purpose

This codebook provides background for the TEDS files, as well as descriptive information for the variables, frequencies of their values, and limitations of the data. For detailed documentation regarding data collected in each state as they correspond to the TEDS data elements, including state-by-state descriptions of exceptions or anomalies in reporting practices, refer to the TEDS Crosswalks available from SAMHSA. The crosswalks are frequently updated as new information becomes available.

## Contents of this Codebook and Data Set

This codebook corresponds to “Treatment Episode Data Set — Admissions (TEDS-A), 2023.” This data set contains records of TEDS admissions to substance use treatment that occurred in 2023. Note that this codebook corresponds to a public use file for TEDS-A, which consists of data characterizing treatment episodes that were recorded at the time of admission. As such, neither this codebook nor the corresponding data file contains any of the elements unique to the TEDS- D, which consists of data characterizing treatment episodes that was recorded at the time of discharge. A full list of the variables that appear in this data set may be found in Appendix A of this codebook. Please note that none of the variables in this data set are weighted, nor are the frequencies for their values as listed in the Variable Descriptions and Frequencies section.

## Universe

The universe for this public use file is TEDS admissions in calendar year 2023 that were received and processed through December 19, 2024.

## Data Collection

For a complete, detailed description of how states are instructed to process and submit TEDS data, please refer to the Combined Substance Use and Mental Health Treatment Episode Data Set (TEDS) State Instruction Manual and the Data Submission System (DSS) State User Manual. If you need copies of these manuals, please contact the BHSIS office at BHSIS_Outreach@hendall.com.

## Confidentiality Protection

Several measures are taken to protect the confidentiality of the TEDS records. Variables that potentially identify an individual in their raw form undergo routine top- or bottom-coding in order to prevent high and low values from distinguishing a respondent’s record. For example, age as a continuous variable has the potential to identify both the youngest and oldest participants in a public release file. For this reason, age is recoded into 11 categories for the public use file to reduce disclosure risk. The youngest category for age combines the ages of 12– 14 years. Similarly, ages of 65 years and older were top-coded. All the variables recoded are documented in Appendix B. Disclosure analysis is used to identify records that remained unique after routine measures were taken to protect confidentiality. Disclosure analysis is used to discern combinations of indirect

identifiers that potentially link an individual to a record. Records identified are classified as subject to disclosure risk using a combination of between seven and eight socio-demographic variables. In order to satisfy stringent confidentiality standards, data swapping is applied to the TEDS using an algorithm that matches, in the following order, for:

- records in a different state, but within the same Census region and division; or, if a match is not found;
- records outside the Census division; or, if still no match is found; and
- records from outside the Census region. If a parallel record is still not found, the combination of socio-demographic characteristics against which to match another record is reduced to between six and seven variables, and the process is repeated until a match is found and swap achieved. Data swapping is implemented to de-identify records in TEDS. This method has several benefits over other disclosure protection options: (1) the overall impact to the data is typically small; (2) nearly all of the data are left intact; (3) data for special populations (e.g., minorities, pregnant women) are no more impacted than other data; (4) the procedures typically do not affect any analytic uses of the file; and (5) the procedures allow greater detail to remain on the public use file (e.g., the original ethnicity codes). The statistical disclosure control (SDC) method employed for TEDS manages disclosure risk below a tolerable risk threshold, while ensuring high-utility, high-quality statistical data.

## Coverage

The TEDS attempts to include all admissions to providers receiving public funding. Because each state or jurisdiction decides the TEDS eligibility of a provider, there is no independent check on the actual sources of funding. Although SAMHSA requests that states submit data on all admissions to any publicly funded treatment facility, reporting in some state agencies is structured so that only clients treated with public funds are included in the TEDS. The number and characteristics of clients in these facilities whose treatment is not publicly funded is unknown.

## Data Limitations

The TEDS, while comprising a significant proportion of all admissions to substance use treatment facilities, does not include all such admissions. The TEDS is a compilation of facility data from state administrative systems. The scope of facilities included in the TEDS is affected by differences in state licensure, certification, accreditation, and disbursement of public funds. For example, some state substance abuse agencies regulate private facilities and individual practitioners, while others do not. In some states, hospital-based substance use treatment facilities are not licensed through the state substance abuse agency. Some state substance abuse agencies track treatment in correctional facilities (state prisons and local jails), while others do not. In general, facilities reporting TEDS data receive state alcohol and/or drug agency funds (including federal block grant funds) for the provision of alcohol and/or drug treatment services. Most states are able to report all admissions to all eligible facilities, although some report only admissions financed by public funds. States may report data from facilities that do not receive public funds, but generally do not because of the difficulty in obtaining data from these facilities.

The TEDS generally does not include data on facilities operated by federal agencies, including the Bureau of Prisons, the Department of Defense, and the Department of Veterans Affairs. However, some facilities operated by the Indian Health Service are included. The primary goal of TEDS is to monitor the characteristics of treatment episodes for people with substance use disorders. Implicit in the concept of treatment is a planned, continuing treatment regimen. Thus, TEDS does not include early intervention programs; these are considered to be prevention programs. Crisis intervention facilities, such as sobering-up stations and hospital emergency departments, are not included in the TEDS. The TEDS is a large and powerful data set. Like all data sets, however, care must be taken that interpretation does not extend beyond the limitations of the data. Limitations fall into two broad categories: those related to the scope of the data collection system, and those related to the difficulties of aggregating data from highly diverse state data collection systems. Limitations to be kept in mind while analyzing TEDS data include:

- The number and client mix of TEDS records depends, to some extent, on external factors, including the availability of public funds. In states with higher funding levels, a larger percentage of the substance-using population may be admitted to treatment, including the less severely impaired and the less economically disadvantaged.
- The primary, secondary, and tertiary substances of use reported to the TEDS are those substances that led to the treatment episode, and not necessarily a complete enumeration of all drugs used at the time of admission.
- The way an admission is defined may vary from state to state, such that the absolute number of admissions is not a valid measure for comparing states.
- States continually review the quality of their data processing. As systematic errors are identified, revisions may be enacted in historical TEDS data files. While this system improves the data set over time, reported historical statistics may change slightly from year to year.
- States vary in the extent to which coercion plays a role in referral to treatment. This variation derives from criminal justice practices and differing concentrations of user subpopulations.
- Public funding constraints may direct states to selectively target special populations—pregnant women or adolescents, for example.
- Many states submit records that include multiple admissions for the same client. Therefore, any statistics derived from the data will represent admissions, not clients. It is possible for clients to have multiple initial admissions within a state—and even within providers that have multiple treatment sites within the state. A few states uniquely identify clients at the state-level; several more are attempting to achieve this level of client identification. The TEDS provides a good national snapshot of what is seen at admission to treatment, but is currently unable to follow individual clients through a sequence of treatment episodes.
- The TEDS distinguishes between transfer admissions and initial admissions. Transfers are admissions of clients transferred for distinct services within an episode of treatment. Only initial admissions are included in the public use files.
- Some states have no opioid treatment programs (OTPs) that provide medication-assisted therapy using methadone, buprenorphine, or naltrexone. Contact the BHSIS office for information regarding data collected by each state.

## Created Variables

The TEDS files contain several variables created from the original variables submitted by the states. For example, a variable was created to indicate whether a given drug was recorded as an admission’s primary, secondary, or tertiary drug of use. These are called flag variables. Their names and labels reflect the drug in question: alcflg for alcohol flag variable, cokeflg for cocaine flag variable, etc. Some variables in the TEDS reports are created by combining or recoding original variables submitted by states. A Technical Note is provided in Appendix C detailing how these variables are derived.

## Formats Available for This Public Use File

The TEDS public use files are provided in SAS, SPSS, Stata, R, and ASCII comma-delimited formats.

## State Exclusions

The following states did not report sufficient data and are excluded from the given years.

| Year | States |
|---|---|
| 2023 | Delaware, South Carolina, West Virginia |

# Variable Descriptions and Frequencies

## CASEID — Case identification number

Program generated case (record) identifier.

*A frequency distribution of this variable is not shown; each case has a unique value generated for identification purposes. Width: 11; Decimal: 0 Variable type: Numeric*

## ADMYR — Year of admission

Year of client's admission to substance use treatment.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 2023 | 2023 | 1,625,833 | 100% |
| | **Total** | **1,625,833** | **100%** |

*Width: 4; Decimal: 0 Variable type: Numeric*

## AGE — Age at admission

Calculated from date of birth and date of admission and then categorized.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | 12-14 years | 9,554 | 0.6% |
| 2 | 15-17 years | 29,956 | 1.8% |
| 3 | 18-20 years | 34,587 | 2.1% |
| 4 | 21-24 years | 89,953 | 5.5% |
| 5 | 25-29 years | 197,042 | 12.1% |
| 6 | 30-34 years | 282,927 | 17.4% |
| 7 | 35-39 years | 262,348 | 16.1% |
| 8 | 40-44 years | 214,270 | 13.2% |
| 9 | 45-49 years | 145,069 | 8.9% |
| 10 | 50-54 years | 129,183 | 7.9% |
| 11 | 55-64 years | 189,852 | 11.7% |
| 12 | 65 years and older | 41,092 | 2.5% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## SEX — Sex

This field identifies the client's biological sex.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Male | 1,060,317 | 65.2% |
| 2 | Female | 564,289 | 34.7% |
| -9 | Missing/unknown/not collected/invalid | 1,227 | 0.1% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## RACE — Race

This field identifies the client's race:

- Alaska Native (Aleut, Eskimo): A person having origins in any of the original people of Alaska. This category may be reported if available.
- American Indian or Alaska Native: A person having origins in any of the original people of North America and South America (including Central America and the original peoples of Alaska) and who maintains Tribal affiliation or community attachment. States collecting Alaska Native information should use this category for all other American Indians.
- Asian or Pacific Islander: A person having origins in any of the original people of the Far East, the Indian subcontinent, Southeast Asia, or the Pacific Islands. This category may be used only if a state does not collect Asian and Native Hawaiian or Other Pacific Islander information separately.
- Black or African American: A person having origins in any of the black racial groups of Africa.
- White: A person having origins in any of the original people of Europe, the Middle East, or North Africa.
- Asian: A person having origins in any of the original people of the Far East, Southeast Asia, or the Indian subcontinent, including, for example, Cambodia, China, India, Japan, Korea, Malaysia, Pakistan, the Philippine Islands, Thailand, and Vietnam.
- Other single race: Use this category for instances in which the client is not identified in any category above or whose origin group because of area custom is regarded as a racial class distinct from the above categories.
- Two or more races: Use this code when the state data system allows multiple race selection and more than one race is indicated.
- Native Hawaiian or Other Pacific Islander: A person having origins in any of the original peoples of Hawaii, Guam, Samoa, or other Pacific Islands.

Guidelines: If the state does not distinguish between American Indian and Alaska Native, code both as 2, American Indian. States that can separate 'Asian' and 'Native Hawaiian or Other Pacific Islander' should use codes 6 and 9 for those categories. States that cannot make the separation should use the combined code 3 until the separation becomes possible. Once a state begins using codes 6 and 9, code 3 should no longer be used by that state. States are asked to convert to the new categories when possible.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Alaska Native (Aleut, Eskimo) | 2,333 | 0.1% |
| 2 | American Indian (other than Alaska Native) | 64,225 | 4.0% |
| 3 | Asian or Pacific Islander | 174 | 0.0% |
| 4 | Black or African American | 301,793 | 18.6% |
| 5 | White | 974,253 | 59.9% |
| 6 | Asian | 11,707 | 0.7% |
| 7 | Other single race | 115,229 | 7.1% |
| 8 | Two or more races | 36,124 | 2.2% |
| 9 | Native Hawaiian or Other Pacific Islander | 5,913 | 0.4% |
| -9 | Missing/unknown/not collected/invalid | 114,082 | 7.0% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## ETHNIC — Ethnicity

This field identifies a client's specific Hispanic or Latino origin, if applicable.

- Puerto Rican: Of Puerto Rican origin regardless of race.
- Mexican: Of Mexican origin regardless of race.
- Cuban: Of Cuban origin regardless of race.
- Other specific Hispanic or Latino: Of known Central or South American or any other Spanish culture or origin (including Spain), other than Puerto Rican, Mexican, or Cuban, regardless of race.
- Not of Hispanic or Latino origin.
- Hispanic, specific origin not specified: Of Hispanic or Latino origin, but origin not known or not specified.

Guidelines: If a state does not collect specific Hispanic detail, this field is coded as 5 - Hispanic or Latino, specific origin not specified.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Puerto Rican | 44,393 | 2.7% |
| 2 | Mexican | 66,829 | 4.1% |
| 3 | Cuban or other specific Hispanic | 52,003 | 3.2% |
| 4 | Not of Hispanic or Latino origin | 1,223,730 | 75.3% |
| 5 | Hispanic or Latino, specific origin not specified | 73,358 | 4.5% |
| -9 | Missing/unknown/not collected/invalid | 165,520 | 10.2% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## MARSTAT — Marital status

This field describes the client's marital status. The following categories are compatible with categories used in the U.S. Census.

- Never married: Includes clients who are single or whose only marriage was annulled.
- Now married: Includes married couples, those living together as married, living with partners, or cohabiting.
- Separated: Includes those legally separated or otherwise absent from spouse because of marital discord.
- Divorced, widowed.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Never married | 790,290 | 48.6% |
| 2 | Now married | 140,458 | 8.6% |
| 3 | Separated | 54,216 | 3.3% |
| 4 | Divorced, widowed | 166,705 | 10.3% |
| -9 | Missing/unknown/not collected/invalid | 474,164 | 29.2% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## EDUC — Education

This field specifies a) the highest school grade completed for adults or children not attending school or b) current school grade for school-age children (3-17 years old) attending school.

Guidelines: States that use specific categories for designating education level should map their categories to a logical number of years of school completed. The mapping should be recorded in the state crosswalk. For example, a state category of 'associate's degree' would be mapped to 4; 'bachelor's degree' would be mapped to 5, etc.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Less than one school grade, no schooling, nursery school, or kindergarten | 78,270 | 4.8% |
| 2 | Grades 9 to 11 | 242,791 | 14.9% |
| 3 | Grade 12 (or GED) | 640,375 | 39.4% |
| 4 | 1-3 years of college, university, or vocational school | 241,150 | 14.8% |
| 5 | 4 years of college, university, BA/BS, some postgraduate study, or more | 82,732 | 5.1% |
| -9 | Missing/unknown/not collected/invalid | 340,515 | 20.9% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## EMPLOY — Employment status

This field identifies the client’s employment status at the time of admission.

- Full-time: Working 35 hours or more each week, including active duty members of the uniformed services.
- Part-time: Working fewer than 35 hours each week.
- Unemployed: Looking for work during the past 30 days or laid off from a job.
- Not in labor force: Not looking for work during the past 30 days or a student, homemaker, disabled, retired, or an inmate of an institution. Clients in this category are further defined in Detailed not in labor force.

Guidelines: Seasonal workers are coded in this category based on their employment status at the time of admission. For example, if they are employed full time at the time of admission, they are coded as 01. If they are not in the labor force at the time of admission, they are coded 04.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Full-time | 276,235 | 17.0% |
| 2 | Part-time | 91,505 | 5.6% |
| 3 | Unemployed | 529,939 | 32.6% |
| 4 | Not in labor force | 457,934 | 28.2% |
| -9 | Missing/unknown/not collected/invalid | 270,220 | 16.6% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## DETNLF — Detailed not in labor force

Provides more detailed information about those clients who are coded as '04 Not in labor force' in Employment Status at the time of admission.

Resident of institution: Persons receiving services from institutional facilities such as hospitals, jails, prisons, long-term residential care, etc.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Homemaker | 7,466 | 0.5% |
| 2 | Student | 35,208 | 2.2% |
| 3 | Retired, disabled | 96,671 | 5.9% |
| 4 | Resident of institution | 29,087 | 1.8% |
| 5 | Other | 227,211 | 14.0% |
| -9 | Missing/unknown/not collected/invalid | 1,230,190 | 75.7% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## PREG — Pregnant at admission

This field indicates whether a female client was pregnant at the time of admission.

Guidelines: All male clients were recoded to missing for this variable due to the item being not applicable.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Yes | 20,862 | 1.3% |
| 2 | No | 473,916 | 29.1% |
| -9 | Missing/unknown/not collected/invalid | 1,131,055 | 69.6% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## VET — Veteran status

This field indicates whether the client has served in the uniformed services (Army, Navy, Air Force, Marine Corps, Coast Guard, Public Health Service Commissioned Corps, Coast and Geodetic Survey, etc.).

Guidelines: A veteran is a person 16 years or older who has served (even for a short time), but is not currently serving, on active duty in the U.S. Army, Navy, Marine Corps, Coast Guard, or Commissioned Corps of the U.S. Public Health Service or National Oceanic and Atmospheric Administration, or who served as a Merchant Marine seaman during World War II. Persons who served in the National Guard or Military Reserves are classified as veterans only if they were ever called or ordered to active duty, not counting the four to six months for initial training or yearly summer camps.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Yes | 33,886 | 2.1% |
| 2 | No | 1,278,705 | 78.6% |
| -9 | Missing/unknown/not collected/invalid | 313,242 | 19.3% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## LIVARAG — Living arrangements

Identifies whether the client is experiencing homelessness, a dependent (living with parents or in a supervised setting), or living independently on their own at the time of admission.

- Experiencing homelessness: Clients with no fixed address; includes homeless shelters.
- Dependent living: Clients living in a supervised setting, such as a residential institution, halfway house, or group home, and children (under age 18) living with parents, relatives, or guardians, or (substance use clients only) in foster care.
- Independent living: Clients living alone or with others in a private residence and capable of self-care. Includes adult children (age 18 and over) living with parents and adolescents living independently. Includes clients who live independently with case management or housing support.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Experiencing homelessness | 252,666 | 15.5% |
| 2 | Dependent living | 225,137 | 13.8% |
| 3 | Independent living | 784,313 | 48.2% |
| -9 | Missing/unknown/not collected/invalid | 363,717 | 22.4% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## PRIMINC — Source of income/support

This field identifies the client’s principal source of financial support. For children younger than 18 years old, report the primary parental source of income/support.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Wages/salary | 348,349 | 21.4% |
| 2 | Public assistance | 88,910 | 5.5% |
| 3 | Retirement/pension, disability | 109,738 | 6.7% |
| 4 | Other | 115,876 | 7.1% |
| 5 | None | 399,819 | 24.6% |
| -9 | Missing/unknown/not collected/invalid | 563,141 | 34.6% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## ARRESTS — Arrests in past 30 days

Indicates the number of arrests in the 30 days prior to the reference date (i.e., date of admission).

Guidelines: This field is intended to capture the number of times the client was arrested (not the number of charges) for any cause during the 30 days preceding the date of admission to treatment. Any formal arrest is to be counted regardless of whether incarceration or conviction resulted and regardless of the status of proceedings incident to the arrest at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | None | 1,152,743 | 70.9% |
| 1 | Once | 80,176 | 4.9% |
| 2 | Two or more times | 16,847 | 1.0% |
| -9 | Missing/unknown/not collected/invalid | 376,067 | 23.1% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## STFIPS — Census state FIPS code

Shows state FIPS codes. These codes are consistent with those used by the U.S. Census Bureau.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Alabama | 14,847 | 0.9% |
| 2 | Alaska | 4,916 | 0.3% |
| 4 | Arizona | 188,265 | 11.6% |
| 5 | Arkansas | 13,937 | 0.9% |
| 6 | California | 114,547 | 7.0% |
| 8 | Colorado | 67,404 | 4.1% |
| 9 | Connecticut | 47,028 | 2.9% |
| 11 | District of Columbia | 2,061 | 0.1% |
| 12 | Florida | 49,620 | 3.1% |
| 13 | Georgia | 33,234 | 2.0% |
| 15 | Hawaii | 869 | 0.1% |
| 16 | Idaho | 230 | 0.0% |
| 17 | Illinois | 38,086 | 2.3% |
| 18 | Indiana | 20,195 | 1.2% |
| 19 | Iowa | 20,309 | 1.2% |
| 20 | Kansas | 8,250 | 0.5% |
| 21 | Kentucky | 11,954 | 0.7% |
| 22 | Louisiana | 13,503 | 0.8% |
| 23 | Maine | 7,242 | 0.4% |
| 24 | Maryland | 144,471 | 8.9% |
| 25 | Massachusetts | 61,109 | 3.8% |
| 26 | Michigan | 66,699 | 4.1% |
| 27 | Minnesota | 65,918 | 4.1% |
| 28 | Mississippi | 6,364 | 0.4% |
| 29 | Missouri | 41,088 | 2.5% |
| 30 | Montana | 676 | 0.0% |
| 31 | Nebraska | 5,795 | 0.4% |
| 32 | Nevada | 9,951 | 0.6% |
| 33 | New Hampshire | 590 | 0.0% |
| 34 | New Jersey | 81,711 | 5.0% |
| 35 | New Mexico | 5,207 | 0.3% |
| 36 | New York | 185,157 | 11.4% |
| 37 | North Carolina | 33,882 | 2.1% |
| 38 | North Dakota | 3,423 | 0.2% |
| 39 | Ohio | 16,251 | 1.0% |
| 40 | Oklahoma | 14,313 | 0.9% |
| 41 | Oregon | 63,919 | 3.9% |
| 42 | Pennsylvania | 18,992 | 1.2% |
| 44 | Rhode Island | 10,459 | 0.6% |
| 46 | South Dakota | 16,011 | 1.0% |
| 47 | Tennessee | 17,373 | 1.1% |
| 48 | Texas | 32,344 | 2.0% |
| 49 | Utah | 11,782 | 0.7% |
| 50 | Vermont | 5,656 | 0.3% |
| 51 | Virginia | 16,649 | 1.0% |
| 53 | Washington | 14,963 | 0.9% |
| 55 | Wisconsin | 12,095 | 0.7% |
| 56 | Wyoming | 4,127 | 0.3% |
| 72 | Puerto Rico | 2,361 | 0.1% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## CBSA2020 — CBSA 2020 code

The term 'Core Based Statistical Area' (CBSA) is a collective term for both metro and micro areas. Metropolitan and micropolitan statistical areas (metro and micro areas) are geographic entities defined by the U.S. Office of Management and Budget (OMB) for use by federal statistical agencies in collecting, tabulating, and publishing federal statistics. A metro area contains a core urban area with a population of at least 50,000, and a micro area contains an urban core with a population of at least 10,000 but less than 50,000. Each metro or micro area consists of one or more counties and includes the counties containing the core urban area, as well as any adjacent counties that have a high degree of social and economic integration (as measured by commuting to work) with the urban core.

Frequencies for this variable are not displayed in the codebook. To view the response categories, please analyze the data file in the statistical package of your choice (SAS, SPSS, STATA, R, ASCII).

*Width: 2; Decimal: 0 Variable type: Numeric*

## REGION — Census region

The geographic regions shown are based on divisions used by the U.S. Census Bureau with the addition of U.S. territories, which are not included in any Census region:

- U.S. territories: Puerto Rico.
- Northeast: New England Division (Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont) and Middle Atlantic Division (New Jersey, New York, Pennsylvania).
- Midwest: East North Central Division (Illinois, Indiana, Michigan, Ohio, Wisconsin) and West North Central Division (Iowa, Kansas, Minnesota, Missouri, Nebraska, North Dakota, South Dakota).
- South: South Atlantic Division (Delaware, District of Columbia, Florida, Georgia, Maryland, North Carolina, South Carolina, Virginia, West Virginia), East South Central Division (Alabama, Kentucky, Mississippi, Tennessee), and West South Central Division (Arkansas, Louisiana, Oklahoma, Texas).
- West: Mountain Division (Arizona, Colorado, Idaho, Montana, Nevada, New Mexico, Utah, Wyoming) and Pacific Division (Alaska, California, Hawaii, Oregon, Washington).

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | U.S. territories | 2,361 | 0.1% |
| 1 | Northeast | 417,944 | 25.7% |
| 2 | Midwest | 314,120 | 19.3% |
| 3 | South | 404,552 | 24.9% |
| 4 | West | 486,856 | 29.9% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## DIVISION — Census division

Census divisions are groupings of states that are subdivisions of the four Census regions. There are nine divisions, which the U.S. Census Bureau adopted in 1910 for the presentation of data. U.S. territories are not included in any Census region or division. The divisions and the states included in them are:

- U.S. territories: Puerto Rico.
- New England: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, and Vermont.
- Middle Atlantic: New Jersey, New York, and Pennsylvania.
- East North Central: Illinois, Indiana, Michigan, Ohio, and Wisconsin.
- West North Central: Iowa, Kansas, Minnesota, Missouri, Nebraska, North Dakota, and South Dakota.
- South Atlantic: Delaware, District of Columbia, Florida, Georgia, Maryland, North Carolina, South Carolina, Virginia, and West Virginia.
- East South Central: Alabama, Kentucky, Mississippi, and Tennessee.
- West South Central: Arkansas, Louisiana, Oklahoma, and Texas.
- Mountain: Arizona, Colorado, Idaho, Montana, Nevada, New Mexico, Utah, and Wyoming.
- Pacific: Alaska, California, Hawaii, Oregon, and Washington.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | U.S. territories | 2,361 | 0.1% |
| 1 | New England | 132,084 | 8.1% |
| 2 | Middle Atlantic | 285,860 | 17.6% |
| 3 | East North Central | 153,326 | 9.4% |
| 4 | West North Central | 160,794 | 9.9% |
| 5 | South Atlantic | 279,917 | 17.2% |
| 6 | East South Central | 50,538 | 3.1% |
| 7 | West South Central | 74,097 | 4.6% |
| 8 | Mountain | 287,642 | 17.7% |
| 9 | Pacific | 199,214 | 12.3% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## SERVICES — Type of treatment service/setting

This field describes the type of treatment service or treatment setting in which the client is placed at the time of admission or transfer.

- Detoxification, 24-hour service, hospital inpatient: 24 hours per day medical acute care services in a hospital setting for detoxification of persons with severe medical complications associated with withdrawal.
- Detoxification, 24-hour service, freestanding residential: 24 hours per day services in a non-hospital setting providing a safe withdrawal environment and transition to ongoing treatment.
- Rehabilitation/Residential, hospital (other than detoxification): 24 hours per day medical care in a hospital facility in conjunction with treatment services for alcohol and other drug use and dependency.
- Rehabilitation/Residential, short term (30 days or fewer): Typically, 30 days or fewer of non-acute care in a setting with treatment services for alcohol and other drug use and dependency.
- Rehabilitation/Residential, long term (more than 30 days): Typically, more than 30 days of non-acute care in a setting with treatment services for alcohol and other drug use and dependency; may include transitional living arrangements such as halfway houses.
- Ambulatory, intensive outpatient: At a minimum, treatment lasting two or more hours per day for three or more days per week.
- Ambulatory, non-intensive outpatient: Ambulatory treatment services including individual, family and/or group services; may include pharmacological therapies.
- Ambulatory, detoxification: Outpatient treatment services providing a safe withdrawal environment in an ambulatory setting (pharmacological or non-pharmacological).

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Detox, 24-hour, hospital inpatient | 33,277 | 2.0% |
| 2 | Detox, 24-hour, free-standing residential | 222,797 | 13.7% |
| 3 | Rehab/residential, hospital (non-detox) | 11,543 | 0.7% |
| 4 | Rehab/residential, short term (30 days or fewer) | 186,278 | 11.5% |
| 5 | Rehab/residential, long term (more than 30 days) | 122,578 | 7.5% |
| 6 | Ambulatory, intensive outpatient | 196,094 | 12.1% |
| 7 | Ambulatory, non-intensive outpatient | 828,477 | 51.0% |
| 8 | Ambulatory, detoxification | 24,789 | 1.5% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## METHUSE — Medication-assisted opioid therapy

This field identifies whether the use of opioid medications, such as methadone, buprenorphine, and/or naltrexone, are part of the client’s treatment plan.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Yes | 237,384 | 14.6% |
| 2 | No | 1,206,672 | 74.2% |
| -9 | Missing/unknown/not collected/invalid | 181,777 | 11.2% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## DAYWAIT — Days waiting to enter substance use treatment

Indicates the number of days from the first contact or request for substance use treatment service until the client was admitted and the first clinical substance use treatment service was provided.

Guidelines: This field is intended to capture the number of days the client must wait to begin treatment because of program capacity, treatment availability, admissions requirements, or other program requirements. It should not include time delays caused by client unavailability or client failure to meet any requirement or obligation.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | 0 | 548,590 | 33.7% |
| 1 | 1-7 | 127,505 | 7.8% |
| 2 | 8-14 | 31,891 | 2.0% |
| 3 | 15-30 | 25,702 | 1.6% |
| 4 | 31 or more | 19,422 | 1.2% |
| -9 | Missing/unknown/not collected/invalid | 872,723 | 53.7% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## PSOURCE — Referral source

This field describes the person or agency referring the client to treatment:

- Individual (includes self-referral): Includes the client, a family member, friend, or any other individual who would not be included in any of the following categories; includes self-referral due to pending DWI/DUI.
- Alcohol/drug use care provider: Any program, clinic, or other health care provider whose principal objective is treating clients with substance use diagnosis, or a program whose activities are related to alcohol or other drug use prevention, education, or treatment.
- Other health care provider: A physician, psychiatrist, or other licensed health care professional; or general hospital, psychiatric hospital, mental health program, or nursing home.
- School (educational): A school principal, counselor, or teacher; or a student assistance program (SAP), the school system, or an educational agency.
- Employer/Employee Assistance Program (EAP): A supervisor or an employee counselor.
- Other community referral: Community or religious organization or any federal, state, or local agency that provides aid in the areas of poverty relief, unemployment, shelter, or social welfare. This category also includes defense attorneys and self-help groups such as Alcoholics Anonymous (AA), Al-Anon, and Narcotics Anonymous (NA).
- Court/criminal justice referral/DUI/DWI: Any police official, judge, prosecutor, probation officer or other person affiliated with a federal, state, or county judicial system. Includes referral by a court for DWI/DUI, clients referred in lieu of or for deferred prosecution, or during pre-trial release, or before or after official adjudication. Includes clients on pre-parole, pre-release, work or home furlough or Treatment Accountability for Safer Communities (TASC). The client need not be officially designated as “on parole.” Includes clients referred through civil commitment. Clients in this category are further defined in Detailed Criminal Justice Referral.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Individual (includes self-referral) | 642,483 | 39.5% |
| 2 | Alcohol/drug use care provider | 117,006 | 7.2% |
| 3 | Other health care provider | 92,868 | 5.7% |
| 4 | School (educational) | 6,248 | 0.4% |
| 5 | Employer/EAP | 9,595 | 0.6% |
| 6 | Other community referral | 107,634 | 6.6% |
| 7 | Court/criminal justice referral/DUI/DWI | 315,967 | 19.4% |
| -9 | Missing/unknown/not collected/invalid | 334,032 | 20.5% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## DETCRIM — Detailed criminal justice referral

This field provides more detailed information about those clients who are coded as '07 Criminal justice referral' in Referral Source at admission.

- State/federal court.
- Other court – Court other than state or federal court.
- Probation/parole.
- Other recognized legal entity – For example, local law enforcement agency, corrections agency, youth services, review board/agency.
- Diversionary program – For example, TASC.
- Prison.
- DUI/DWI.
- Other.

Guidelines: This field is to be used only if the principal source of referral in the Minimum Data Set field is coded 07, 'criminal justice referral.' For all other principal source of referral codes (01 to 06 and missing), this field should be coded as missing.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | State/federal court | 32,467 | 2.0% |
| 2 | Formal adjudication process | 15,602 | 1.0% |
| 3 | Probation/parole | 85,026 | 5.2% |
| 4 | Other recognized legal entity | 30,829 | 1.9% |
| 5 | Diversionary program | 8,027 | 0.5% |
| 6 | Prison | 6,794 | 0.4% |
| 7 | DUI/DWI | 26,298 | 1.6% |
| 8 | Other | 17,223 | 1.1% |
| -9 | Missing/unknown/not collected/invalid | 1,403,567 | 86.3% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## NOPRIOR — Previous substance use treatment episodes

Indicates the number of previous treatment episodes the client has received in any substance use treatment program. Changes in service for the same episode (transfers) should not be counted as separate prior episodes.

Guidelines: This field measures the substance use treatment history of the client only. This does not include or pertain to the client's mental health treatment history. It is preferred that the number of prior treatments be a self-reported field collected at the time of client intake. However, this data field may be derived from the state data system, if the system has that capability, and episodes can be counted for several years.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | No prior treatment episodes | 459,972 | 28.3% |
| 1 | One prior treatment episode | 288,604 | 17.8% |
| 2 | Two prior treatment episodes | 197,208 | 12.1% |
| 3 | Three prior treatment episodes | 123,995 | 7.6% |
| 4 | Four prior treatment episodes | 83,811 | 5.2% |
| 5 | Five or more prior treatment episodes | 285,287 | 17.5% |
| -9 | Missing/unknown/not collected/invalid | 186,956 | 11.5% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## SUB1 — Substance use (primary)

This field identifies the client's primary substance use at admission.

(1) None. (2) Alcohol. (3) Cocaine/crack. (4) Marijuana/hashish: Includes THC and any other cannabis sativa preparations. (5) Heroin. (6) Non-prescription methadone. (7) Other opiates and synthetics: Includes buprenorphine, butorphanol, codeine, hydrocodone, hydromorphone, meperidine, morphine, opium, oxycodone, pentazocine, propoxyphene, tramadol, and other narcotic analgesics, opiates, or synthetics. (8) PCP: Phencyclidine. (9) Hallucinogens: Includes LSD, DMT, mescaline, peyote, psilocybin, STP, and other hallucinogens. (10) Methamphetamine/speed. (11) Other amphetamines: Includes amphetamines, MDMA, ‘bath salts’, phenmetrazine, and other amines and related drugs. (12) Other stimulants: Includes methylphenidate and any other stimulants. (13) Benzodiazepines: Includes alprazolam, chlordiazepoxide, clonazepam, clorazepate, diazepam, flunitrazepam, flurazepam, halazepam, lorazepam, oxazepam, prazepam, temazepam, triazolam, and other unspecified benzodiazepines. (14) Other tranquilizers: Includes meprobamate, and other non-benzodiazepine tranquilizers. (15) Barbiturates: Includes amobarbital, pentobarbital, phenobarbital, secobarbital, etc. (16) Other sedatives or hypnotics: Includes chloral hydrate, ethchlorvynol, glutethimide, methaqualone, and other non-barbiturate sedatives and hypnotics. (17) Inhalants: Includes aerosols; chloroform, ether, nitrous oxide and other anesthetics; gasoline; glue; nitrites; paint thinner and other solvents; and other inappropriately inhaled products. (18) Over-the-counter medications: Includes aspirin, dextromethorphan and other cough syrups, diphenhydramine and other anti-histamines, ephedrine, sleep aids, and any other legally obtained, non-prescription medication. (19) Other drugs: Includes diphenylhydantoin/phenytoin, GHB/GBL, ketamine, synthetic cannabinoid 'Spice', carisoprodol (Soma), and other drugs.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | None | 58,808 | 3.6% |
| 2 | Alcohol | 474,586 | 29.2% |
| 3 | Cocaine/crack | 89,763 | 5.5% |
| 4 | Marijuana/hashish | 123,350 | 7.6% |
| 5 | Heroin | 177,111 | 10.9% |
| 6 | Non-prescription methadone | 1,229 | 0.1% |
| 7 | Other opiates and synthetics | 174,679 | 10.7% |
| 8 | PCP | 2,914 | 0.2% |
| 9 | Hallucinogens | 2,083 | 0.1% |
| 10 | Methamphetamine/speed | 188,620 | 11.6% |
| 11 | Other amphetamines | 10,115 | 0.6% |
| 12 | Other stimulants | 3,140 | 0.2% |
| 13 | Benzodiazepines | 11,095 | 0.7% |
| 14 | Other tranquilizers | 142 | 0.0% |
| 15 | Barbiturates | 720 | 0.0% |
| 16 | Other sedatives or hypnotics | 1,499 | 0.1% |
| 17 | Inhalants | 743 | 0.0% |
| 18 | Over-the-counter medications | 476 | 0.0% |
| 19 | Other drugs | 8,150 | 0.5% |
| -9 | Missing/unknown/not collected/invalid | 296,610 | 18.2% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## ROUTE1 — Route of administration (primary)

This field identifies the usual route of administration of the corresponding substance identified in Substance Use (SUB1).

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Oral | 552,719 | 34.0% |
| 2 | Smoking | 372,708 | 22.9% |
| 3 | Inhalation | 163,369 | 10.0% |
| 4 | Injection (intravenous, intramuscular, intradermal, or subcutaneous) | 155,628 | 9.6% |
| 5 | Other | 9,943 | 0.6% |
| -9 | Missing/unknown/not collected/invalid | 371,466 | 22.8% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## FREQ1 — Frequency of use (primary)

Specifies the frequency of use of the corresponding substance identified in Substance Use (SUB1).

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | No use in the past month | 356,845 | 21.9% |
| 2 | Some use | 348,286 | 21.4% |
| 3 | Daily use | 543,238 | 33.4% |
| -9 | Missing/unknown/not collected/invalid | 377,464 | 23.2% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## FRSTUSE1 — Age at first use (primary)

For alcohol use, this is the age of first intoxication. For substances other than alcohol, this field identifies the age at which the client first used the corresponding substance identified in Substance Use (SUB1).

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | 11 years and under | 67,326 | 4.1% |
| 2 | 12-14 years | 212,558 | 13.1% |
| 3 | 15-17 years | 299,446 | 18.4% |
| 4 | 18-20 years | 221,646 | 13.6% |
| 5 | 21-24 years | 141,686 | 8.7% |
| 6 | 25-29 years | 105,175 | 6.5% |
| 7 | 30 years and older | 165,969 | 10.2% |
| -9 | Missing/unknown/not collected/invalid | 412,027 | 25.3% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## SUB2 — Substance use (secondary)

This field identifies the client's secondary substance use at admission.

(1) None. (2) Alcohol. (3) Cocaine/crack. (4) Marijuana/hashish: Includes THC and any other cannabis sativa preparations. (5) Heroin. (6) Non-prescription methadone. (7) Other opiates and synthetics: Includes buprenorphine, butorphanol, codeine, hydrocodone, hydromorphone, meperidine, morphine, opium, oxycodone, pentazocine, propoxyphene, tramadol, and other narcotic analgesics, opiates, or synthetics. (8) PCP: Phencyclidine. (9) Hallucinogens: Includes LSD, DMT, mescaline, peyote, psilocybin, STP, and other hallucinogens. (10) Methamphetamine/speed. (11) Other amphetamines: Includes amphetamines, MDMA, ‘bath salts’, phenmetrazine, and other amines and related drugs. (12) Other stimulants: Includes methylphenidate and any other stimulants. (13) Benzodiazepines: Includes alprazolam, chlordiazepoxide, clonazepam, clorazepate, diazepam, flunitrazepam, flurazepam, halazepam, lorazepam, oxazepam, prazepam, temazepam, triazolam, and other unspecified benzodiazepines. (14) Other tranquilizers: Includes meprobamate, and other non-benzodiazepine tranquilizers. (15) Barbiturates: Includes amobarbital, pentobarbital, phenobarbital, secobarbital, etc. (16) Other sedatives or hypnotics: Includes chloral hydrate, ethchlorvynol, glutethimide, methaqualone, and other non-barbiturate sedatives and hypnotics. (17) Inhalants: Includes aerosols; chloroform, ether, nitrous oxide and other anesthetics; gasoline; glue; nitrites; paint thinner and other solvents; and other inappropriately inhaled products. (18) Over-the-counter medications: Includes aspirin, dextromethorphan and other cough syrups, diphenhydramine and other anti-histamines, ephedrine, sleep aids, and any other legally obtained, non-prescription medication. (19) Other drugs: Includes diphenylhydantoin/phenytoin, GHB/GBL, ketamine, synthetic cannabinoid 'Spice', carisoprodol (Soma), and other drugs.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | None | 877,370 | 54.0% |
| 2 | Alcohol | 100,062 | 6.2% |
| 3 | Cocaine/crack | 135,622 | 8.3% |
| 4 | Marijuana/hashish | 176,251 | 10.8% |
| 5 | Heroin | 43,060 | 2.6% |
| 6 | Non-prescription methadone | 1,173 | 0.1% |
| 7 | Other opiates and synthetics | 45,696 | 2.8% |
| 8 | PCP | 2,119 | 0.1% |
| 9 | Hallucinogens | 3,208 | 0.2% |
| 10 | Methamphetamine/speed | 106,068 | 6.5% |
| 11 | Other amphetamines | 7,224 | 0.4% |
| 12 | Other stimulants | 3,625 | 0.2% |
| 13 | Benzodiazepines | 24,593 | 1.5% |
| 14 | Other tranquilizers | 204 | 0.0% |
| 15 | Barbiturates | 344 | 0.0% |
| 16 | Other sedatives or hypnotics | 2,278 | 0.1% |
| 17 | Inhalants | 598 | 0.0% |
| 18 | Over-the-counter medications | 887 | 0.1% |
| 19 | Other drugs | 15,631 | 1.0% |
| -9 | Missing/unknown/not collected/invalid | 79,820 | 4.9% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## ROUTE2 — Route of administration (secondary)

This field identifies the usual route of administration of the corresponding substance identified in Substance Use (SUB2).

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Oral | 163,982 | 10.1% |
| 2 | Smoking | 332,194 | 20.4% |
| 3 | Inhalation | 92,796 | 5.7% |
| 4 | Injection (intravenous, intramuscular, intradermal, or subcutaneous) | 65,047 | 4.0% |
| 5 | Other | 8,092 | 0.5% |
| -9 | Missing/unknown/not collected/invalid | 963,722 | 59.3% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## FREQ2 — Frequency of use (secondary)

Specifies the frequency of use of the corresponding substance identified in Substance Use (SUB2).

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | No use in the past month | 213,001 | 13.1% |
| 2 | Some use | 208,884 | 12.8% |
| 3 | Daily use | 239,313 | 14.7% |
| -9 | Missing/unknown/not collected/invalid | 964,635 | 59.3% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## FRSTUSE2 — Age at first use (secondary)

For alcohol use, this is the age of first intoxication. For substances other than alcohol, this field identifies the age at which the client first used the corresponding substance identified in Substance Use (SUB2).

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | 11 years and under | 35,934 | 2.2% |
| 2 | 12-14 years | 117,651 | 7.2% |
| 3 | 15-17 years | 155,548 | 9.6% |
| 4 | 18-20 years | 111,501 | 6.9% |
| 5 | 21-24 years | 66,464 | 4.1% |
| 6 | 25-29 years | 56,442 | 3.5% |
| 7 | 30 years and older | 85,349 | 5.2% |
| -9 | Missing/unknown/not collected/invalid | 996,944 | 61.3% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## SUB3 — Substance use (tertiary)

This field identifies the client's tertiary substance use at admission.

(1) None. (2) Alcohol. (3) Cocaine/crack. (4) Marijuana/hashish: Includes THC and any other cannabis sativa preparations. (5) Heroin. (6) Non-prescription methadone. (7) Other opiates and synthetics: Includes buprenorphine, butorphanol, codeine, hydrocodone, hydromorphone, meperidine, morphine, opium, oxycodone, pentazocine, propoxyphene, tramadol, and other narcotic analgesics, opiates, or synthetics. (8) PCP: Phencyclidine. (9) Hallucinogens: Includes LSD, DMT, mescaline, peyote, psilocybin, STP, and other hallucinogens. (10) Methamphetamine/speed. (11) Other amphetamines: Includes amphetamines, MDMA, ‘bath salts’, phenmetrazine, and other amines and related drugs. (12) Other stimulants: Includes methylphenidate and any other stimulants. (13) Benzodiazepines: Includes alprazolam, chlordiazepoxide, clonazepam, clorazepate, diazepam, flunitrazepam, flurazepam, halazepam, lorazepam, oxazepam, prazepam, temazepam, triazolam, and other unspecified benzodiazepines. (14) Other tranquilizers: Includes meprobamate, and other non-benzodiazepine tranquilizers. (15) Barbiturates: Includes amobarbital, pentobarbital, phenobarbital, secobarbital, etc. (16) Other sedatives or hypnotics: Includes chloral hydrate, ethchlorvynol, glutethimide, methaqualone, and other non-barbiturate sedatives and hypnotics. (17) Inhalants: Includes aerosols; chloroform, ether, nitrous oxide and other anesthetics; gasoline; glue; nitrites; paint thinner and other solvents; and other inappropriately inhaled products. (18) Over-the-counter medications: Includes aspirin, dextromethorphan and other cough syrups, diphenhydramine and other anti-histamines, ephedrine, sleep aids, and any other legally obtained, non-prescription medication. (19) Other drugs: Includes diphenylhydantoin/phenytoin, GHB/GBL, ketamine, synthetic cannabinoid 'Spice', carisoprodol (Soma), and other drugs.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | None | 1,232,128 | 75.8% |
| 2 | Alcohol | 36,358 | 2.2% |
| 3 | Cocaine/crack | 36,432 | 2.2% |
| 4 | Marijuana/hashish | 67,298 | 4.1% |
| 5 | Heroin | 12,260 | 0.8% |
| 6 | Non-prescription methadone | 583 | 0.0% |
| 7 | Other opiates and synthetics | 16,728 | 1.0% |
| 8 | PCP | 1,338 | 0.1% |
| 9 | Hallucinogens | 3,415 | 0.2% |
| 10 | Methamphetamine/speed | 22,337 | 1.4% |
| 11 | Other amphetamines | 3,613 | 0.2% |
| 12 | Other stimulants | 2,827 | 0.2% |
| 13 | Benzodiazepines | 14,107 | 0.9% |
| 14 | Other tranquilizers | 94 | 0.0% |
| 15 | Barbiturates | 204 | 0.0% |
| 16 | Other sedatives or hypnotics | 1,183 | 0.1% |
| 17 | Inhalants | 376 | 0.0% |
| 18 | Over-the-counter medications | 753 | 0.0% |
| 19 | Other drugs | 14,962 | 0.9% |
| -9 | Missing/unknown/not collected/invalid | 158,837 | 9.8% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## ROUTE3 — Route of administration (tertiary)

This field identifies the usual route of administration of the corresponding substance identified in Substance Use (SUB3).

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Oral | 70,348 | 4.3% |
| 2 | Smoking | 114,194 | 7.0% |
| 3 | Inhalation | 31,831 | 2.0% |
| 4 | Injection (intravenous, intramuscular, intradermal, or subcutaneous) | 18,615 | 1.1% |
| 5 | Other | 2,203 | 0.1% |
| -9 | Missing/unknown/not collected/invalid | 1,388,642 | 85.4% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## FREQ3 — Frequency of use (tertiary)

Specifies the frequency of use of the corresponding substance identified in Substance Use (SUB3).

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | No use in the past month | 86,445 | 5.3% |
| 2 | Some use | 69,593 | 4.3% |
| 3 | Daily use | 82,439 | 5.1% |
| -9 | Missing/unknown/not collected/invalid | 1,387,356 | 85.3% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## FRSTUSE3 — Age at first use (tertiary)

For alcohol use, this is the age of first intoxication. For substances other than alcohol, this field identifies the age at which the client first used the corresponding substance identified in Substance Use (SUB3).

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | 11 years and under | 17,010 | 1.0% |
| 2 | 12-14 years | 49,810 | 3.1% |
| 3 | 15-17 years | 57,791 | 3.6% |
| 4 | 18-20 years | 37,626 | 2.3% |
| 5 | 21-24 years | 21,060 | 1.3% |
| 6 | 25-29 years | 17,089 | 1.1% |
| 7 | 30 years and older | 26,875 | 1.7% |
| -9 | Missing/unknown/not collected/invalid | 1,398,572 | 86.0% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## IDU — Current IV drug use reported at admission

Flag records if at least one valid primary, secondary, or tertiary substance was reported and if injection was reported in the corresponding primary, secondary, or tertiary substances' route of administration.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | IDU not reported | 1,079,679 | 66.4% |
| 1 | IDU reported | 190,766 | 11.7% |
| -9 | No substances reported | 355,388 | 21.9% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## ALCFLG — Alcohol reported at admission

Flag records if alcohol was reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,014,827 | 62.4% |
| 1 | Substance reported | 611,006 | 37.6% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## COKEFLG — Cocaine/crack reported at admission

Flag records if cocaine or crack was reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,364,016 | 83.9% |
| 1 | Substance reported | 261,817 | 16.1% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## MARFLG — Marijuana/hashish reported at admission

Flag records if marijuana or hashish were reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,258,934 | 77.4% |
| 1 | Substance reported | 366,899 | 22.6% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## HERFLG — Heroin reported at admission

Flag records if heroin was reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,393,402 | 85.7% |
| 1 | Substance reported | 232,431 | 14.3% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## METHFLG — Non-Rx methadone reported at admission

Flag records if non-prescription methadone was reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,622,848 | 99.8% |
| 1 | Substance reported | 2,985 | 0.2% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## OPSYNFLG — Other opiates/synthetics reported at admission

Flag records if other opiates or synthetics were reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,388,730 | 85.4% |
| 1 | Substance reported | 237,103 | 14.6% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## PCPFLG — PCP reported at admission

Flag records if PCP was reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,619,462 | 99.6% |
| 1 | Substance reported | 6,371 | 0.4% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## HALLFLG — Hallucinogens reported at admission

Flag records if hallucinogens were reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,617,127 | 99.5% |
| 1 | Substance reported | 8,706 | 0.5% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## MTHAMFLG — Methamphetamine/speed reported at admission

Flag records if methamphetamine or speed was reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,308,808 | 80.5% |
| 1 | Substance reported | 317,025 | 19.5% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## AMPHFLG — Other amphetamines reported at admission

Flag records if other amphetamines were reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,604,881 | 98.7% |
| 1 | Substance reported | 20,952 | 1.3% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## STIMFLG — Other stimulants reported at admission

Flag records if other stimulants were reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,616,241 | 99.4% |
| 1 | Substance reported | 9,592 | 0.6% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## BENZFLG — Benzodiazepines reported at admission

Flag records if benzodiazepines were reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,576,038 | 96.9% |
| 1 | Substance reported | 49,795 | 3.1% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## TRNQFLG — Other tranquilizers reported at admission

Flag records if other tranquilizers were reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,625,393 | 100% |
| 1 | Substance reported | 440 | 0.0% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## BARBFLG — Barbiturates reported at admission

Flag records if barbiturates were reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,624,565 | 99.9% |
| 1 | Substance reported | 1,268 | 0.1% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## SEDHPFLG — Other sedatives/hypnotics reported at admission

Flag records if other sedatives or hypnotics were reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,620,873 | 99.7% |
| 1 | Substance reported | 4,960 | 0.3% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## INHFLG — Inhalants reported at admission

Flag records if inhalants were reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,624,116 | 99.9% |
| 1 | Substance reported | 1,717 | 0.1% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## OTCFLG — Over-the-counter medication reported at admission

Flag records if over-the-counter medication were reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,623,717 | 99.9% |
| 1 | Substance reported | 2,116 | 0.1% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## OTHERFLG — Other drug reported at admission

Flag records if other substances were reported as the primary, secondary, or tertiary substance at the time of admission.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | Substance not reported | 1,587,090 | 97.6% |
| 1 | Substance reported | 38,743 | 2.4% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## ALCDRUG — Substance use type

Classifies a client's substance use disorder as alcohol only, other drugs only, alcohol and other drugs, or none. This variable looks across primary, secondary, and tertiary substances reported at the time of admission to treatment.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 0 | None | 355,388 | 21.9% |
| 1 | Alcohol only | 266,143 | 16.4% |
| 2 | Other drugs only | 659,439 | 40.6% |
| 3 | Alcohol and other drugs | 344,863 | 21.2% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## DSMCRIT — DSM diagnosis (SuDS 4 or SuDS 19)

DSM diagnosis codes identify the reason for a client's encounter or treatment. The diagnoses of substance use disorder can be reported using either the Diagnostic and Statistical Manual of Mental Disorders (DSM) from the American Psychiatric Association or the International Classification of Diseases (ICD), from the World Health Organization.

The discrete diagnosis codes have been grouped into categories related to the use of and dependence on specific substances, mental health conditions, and other conditions. Diagnoses reported by states using either standard classification of mental disorders have been combined.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Alcohol-induced disorder | 8,564 | 0.5% |
| 2 | Substance-induced disorder | 34,033 | 2.1% |
| 3 | Alcohol intoxication | 30,278 | 1.9% |
| 4 | Alcohol dependence | 302,899 | 18.6% |
| 5 | Opioid dependence | 335,892 | 20.7% |
| 6 | Cocaine dependence | 61,967 | 3.8% |
| 7 | Cannabis dependence | 62,162 | 3.8% |
| 8 | Other substance dependence | 143,361 | 8.8% |
| 9 | Alcohol abuse | 59,744 | 3.7% |
| 10 | Cannabis abuse | 32,356 | 2.0% |
| 11 | Other substance abuse | 26,085 | 1.6% |
| 12 | Opioid abuse | 20,331 | 1.3% |
| 13 | Cocaine abuse | 9,070 | 0.6% |
| 14 | Anxiety disorders | 2,667 | 0.2% |
| 15 | Depressive disorders | 4,030 | 0.2% |
| 16 | Schizophrenia/other psychotic disorders | 1,095 | 0.1% |
| 17 | Bipolar disorders | 1,670 | 0.1% |
| 18 | Attention deficit/disruptive behavior disorders | 605 | 0.0% |
| 19 | Other mental health condition | 165,050 | 10.2% |
| -9 | Missing/unknown/not collected/invalid/no or deferred diagnosis | 323,974 | 19.9% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## PSYPROB — Co-occurring mental and substance use disorders

Indicates whether the client has co-occurring mental and substance use disorders.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Yes | 686,928 | 42.3% |
| 2 | No | 709,223 | 43.6% |
| -9 | Missing/unknown/not collected/invalid | 229,682 | 14.1% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## HLTHINS — Health insurance

This field specifies the client's health insurance at admission. The insurance may or may not cover behavioral health treatment. Reporting of this field is optional for both substance use and mental health clients. States are encouraged to report data for all categories in the list of valid entries, but reporting a subset of the categories is acceptable. Health insurance should be reported, if collected, whether or not it covers behavioral health treatment.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Private insurance, Blue Cross/Blue Shield, HMO | 68,105 | 4.2% |
| 2 | Medicaid | 617,226 | 38.0% |
| 3 | Medicare, other (e.g. TRICARE, CHAMPUS) | 62,022 | 3.8% |
| 4 | None | 197,003 | 12.1% |
| -9 | Missing/unknown/not collected/invalid | 681,477 | 41.9% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## PRIMPAY — Payment source, primary (expected or actual)

This field identifies the primary source of payment for this treatment episode anticipated at the time of admission.

Guidelines: States operating under a split payment fee arrangement between multiple payment sources are to default to the payment source with the largest percentage. When payment percentages are equal, the state can select either source. Reporting of this field is optional for both substance use and mental health treatment clients. States are encouraged to report data for all categories in the list of valid entries, but reporting a subset of the categories is acceptable.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | Self-pay | 53,264 | 3.3% |
| 2 | Private insurance (Blue Cross/Blue Shield, other health insurance, | 44,300 | 2.7% |
| 3 | Medicare | 22,687 | 1.4% |
| 4 | Medicaid | 464,951 | 28.6% |
| 5 | Other government payments | 130,387 | 8.0% |
| 6 | No charge (free, charity, special research, teaching) | 17,395 | 1.1% |
| 7 | Other | 25,152 | 1.5% |
| -9 | Missing/unknown/not collected/invalid | 867,697 | 53.4% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

## FREQ_ATND_SELF_HELP — Attendance at substance use self-help groups in past 30 days

This field indicates the frequency of attendance at a substance use self-help group in the 30 days prior to the reference date (the date of admission). It includes attendance at Alcoholics Anonymous (AA), Narcotics Anonymous (NA), and other self-help/mutual support groups focused on recovery from substance use and dependence.

Guidelines: For admission records, the reference period is the 30 days prior to admission. The category '5: Some attendance' only applies if it is known that the client attended a self-help program during the reference period, but there is insufficient information to assign a specific frequency.

| Value | Label | Frequency | % |
|---:|---|---:|---:|
| 1 | No attendance | 906,681 | 55.8% |
| 2 | 1-3 times in the past month | 68,630 | 4.2% |
| 3 | 4-7 times in the past month | 44,303 | 2.7% |
| 4 | 8-30 times in the past month | 112,251 | 6.9% |
| 5 | Some attendance, frequency is unknown | 50,609 | 3.1% |
| -9 | Missing/unknown/not collected/invalid | 443,359 | 27.3% |
| | **Total** | **1,625,833** | **100%** |

*Width: 2; Decimal: 0 Variable type: Numeric*

# Appendices

## Appendix A. TEDS-A Variable Information (Alphabetical Order)

| Variable | Type | Length | Label |
|---|---|---:|---|

## Appendix B. Variable Recode Table

### AGE — Age at admission

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
|  | Continuous (0–95) | 1 | 12–14 years |
|  |  | 2 | 15–17 years |
|  |  | 3 | 18–20 years |
|  |  | 4 | 21–24 years |
|  |  | 5 | 25–29 years |
|  |  | 6 | 30–34 years |
|  |  | 7 | 35–39 years |
|  |  | 8 | 40–44 years |
|  |  | 9 | 45–49 years |
|  |  | 10 | 50–54 years |
|  |  | 11 | 55–64 years |
|  |  | 12 | 65–95 years |

### ARRESTS — Number of arrests in the 30 days prior to admission

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
|  | Continuous (0–96) | 0 | None |
|  |  | 1 | Once |
|  |  | 2 | Two or more times |

### ETHNIC — Hispanic or Latino origin (ethnicity)

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
| 1 | Puerto Rico | 1 | Puerto Rico |
| 2 | Mexican | 2 | Mexican |
| 3 | Cuban | 3 | Cuban, other specific Hispanic |
| 4 | Other specific Hispanic | 4 | Not of Hispanic origin |
| 5 | Not of Hispanic origin | 5 | Hispanic, specific origin not specified |
| 6 | Hispanic, specific origin not specified |  |  |

### MARSTAT — Marital status

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
| 1 | Never married | 1 | Never married |
| 2 | Now married | 2 | Now married |
| 3 | Separated | 3 | Separated |
| 4 | Divorced | 4 | Divorced, widowed |
| 5 | Widowed |  |  |

### EDUC — Education

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
|  | Continuous (0–25) | 1 | Less than one school grade, no schooling, nursery school, or kindergarten to Grade 8 |
| 70 | Graduate or professional school | 2 | Grades 9 to 11 |
| 71 | Vocational school | 3 | Grade 12 (or GED) |
| 72 | Nursery school, pre-school | 4 | 1-3 years of college, university, or vocational school |
| 73 | Kindergarten | 5 | 4 years of college, university, BA/BS, some postgraduate study, or more |

### DETNLF — Detailed ‘not in labor’ force category at admission

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
| 1 | Homemaker | 1 | Homemaker |
| 2 | Student | 2 | Student |
| 3 | Retired | 3 | Retired, disabled |
| 4 | Disabled | 4 | Resident of institution |
| 5 | Resident of institution | 5 | Other |
| 6 | Other |  |  |

### PRIMINC — Source of income/support

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
| 1 | Wages/salary | 1 | Wages/salary |
| 2 | Public assistance | 2 | Public assistance |
| 3 | Retirement/pension | 3 | Retirement/pension, disability |
| 4 | Disability | 4 | Other |
| 20 | Other | 5 | None |
| 21 | None |  |  |

### CBSA2020 — Metropolitan or micropolitan statistical area

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
|  | Census CBSA geographic codes |  | When CBSA population is less than 100,000 or is missing, records are recoded as: “Undesignated area/missing/unknown/not collected/ invalid” |

### DAYWAIT — Number of days waiting to enter treatment

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
|  | Continuous (0–996) | 0 | None |
|  |  | 1 | 1–7 days |
|  |  | 2 | 8–14 days |
|  |  | 3 | 15–30 days |
|  |  | 4 | 31 days and more |

### HLTHINS — Health insurance at admission

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
| 1 | Private insurance (other than BC/BS or HMO) | 1 | Private insurance, Blue Cross/Blue Shield, HMO |
| 2 | Blue Cross/Blue Shield (BC/BS) | 2 | Medicaid |
| 3 | Medicare | 3 | Medicare/other (e.g., TRICARE, CHAMPUS) |
| 4 | Medicaid | 4 | None |
| 6 | Health maintenance organization (HMO) |  |  |
| 20 | Other (e.g., TRICARE, CHAMPUS) |  |  |
| 21 | None |  |  |

### PRIMPAY — Primary source of payment for treatment

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
| 1 | Self-pay | 1 | Self-pay |
| 2 | Blue Cross/Blue Shield | 2 | Blue Cross/Blue Shield, other health insurance companies, worker’s compensation |
| 3 | Medicare | 3 | Medicare |
| 4 | Medicaid | 4 | Medicaid |
| 5 | Other government payments | 5 | Other government payments |
| 6 | Worker’s compensation | 6 | No charge (free, charity, special research, or teaching) |
| 7 | Other health insurance companies | 7 | Other |
| 8 | No charge (free, charity, special research, or teaching) |  |  |
| 9 | Other |  |  |

### FREQ_ATND_SELF_HELP — Frequency of attendance at substance use self-help groups in the 30 days prior to admission

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
| 1 | No attendance | 1 | No attendance |
| 2 | Less than once a week | 2 | 1–3 times in the past month |
| 3 | About once a week | 3 | 4–7 times in the past month |
| 4 | 2 to 3 times a week | 4 | 8–30 times in the past month |
| 5 | At least 4 times a week | 5 | Some attendance, frequency is unknown |
| 6 | Some attendance |  |  |

### FREQ1 — Frequency of use at admission (primary substance)

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
| 1 | No use in the past month | 1 | No use |
| 2 | 1–3 days in the past month | 2 | Some use |
| 3 | 1–2 days in the past month | 3 | Daily use |

### FREQ2 — Frequency of use at admission (secondary substance)

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
| 4 | 3–6 days in the past month |  |  |
| 5 | Daily |  |  |

### FREQ3 — Frequency of use at admission (tertiary substance)

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|

### FRSTUSE1 — Age at first use (primary substance)

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
|  | Continuous (0–95) | 1 | 11 years and under 12– |
|  |  | 2 | 14 years |
|  |  | 3 | 15–17 years |

### FRSTUSE2 — Age at first use (secondary substance)

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
|  |  | 4 | 18–20 years |
|  |  | 5 | 21–24 years |
|  |  | 6 | 25–29 years |

### FRSTUSE3 — Age at first use (tertiary substance)

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
|  |  | 7 | 30–95 years |

### DSMCRIT

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
|  | 291.00 – 291.99; F10.14 – F10.99 | 1 | Alcohol-induced disorder |

### DSM — diagnosis (SuDS 4 or SuDS 19)

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
|  | 292.00 – 292.99; F11.14 – F11.99, F12.15 – F12.99, F13.14 – F13.99, F14.14 – F14.99, F15.14 – F15.99, F16.14 – F16.99, F17.208 –F17.299, F18.14 – F18.99, F19.14 – F19.99 303.00 – 303.89; F10.12 – F10.129, F10.22 – F10.229, F10.92 – F10.929 303.90 – 303.99; F10.2 – F10.23 304.00 – 304.09; F11.2 – F11.23 304.20 – 304.29; F14.2 – F14.23 304.30 – 304.39; F12.2 – F12.22 304.10 – 304.19, 304.40 – 304.99, 305.10 – 305.19; F13.2 – F13.23, F15.2 – F15.23, F16.2 – F16.22, F17.2 – F17.293, F18.2 – F18.22, F19.2 – F19.23 305.00 – 305.09; F10.1 – F10.11 305.20 – 305.29; F12.1 – F12.12, F12.9 – F12.92 305.30 – 305.49, 305.70 – 305.99; F13.1 – F13.12, F13.9 – F13.93, F15.1 – F15.12, F15.9 – F15.92, F16.1 – F16.12, F16.9 – F16.92, F18.1 – F18.12, F18.9 – F18.92, F19.1 – F19.12, F19.9 – F19.92 305.50 – 305.59; F11.1 – F11.12, F11.9 – F11.93 | 2 | Substance-induced disorder |
|  |  | 3 | Alcohol intoxication |
|  |  | 4 | Alcohol dependence |
|  |  | 5 | Opioid dependence |
|  |  | 6 | Cocaine dependence |
|  |  | 7 | Cannabis dependence |
|  |  | 8 | Other substance dependence |
|  |  | 9 | Alcohol abuse |
|  |  | 10 | Cannabis abuse |
|  |  | 11 | Other substance abuse |
|  |  | 12 | Opioid abuse |

### DSMCRIT

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
|  | 305.60 – 305.69; | 13 | Cocaine abuse |

### DSM — diagnosis (SuDS 4 or SuDS 19)

| Original code | Original label | Recode | Recoded label |
|---:|---|---:|---|
|  | F14.1 – F14.12, F14.9 – F14.92 293.89, 300.00 – 300.02, 300.21 – 300.23, 300.29 – 300.39, 308.30 – 308.39, 309.81; F06.4, F40 – F43, F48.8, F48.9, R45.2 – R45.84 296.20 – 296.39, 300.40 – 300.49, 311.00 – 311.09; F32 – F32.9, F33 – F33.9 293.81 – 293.82, 295.00 – 295.99, 297.10 – 297.19, 297.30 – 297.39, 298.80 – 298.89, 298.90 – 298.99; F20 – F25, F28 – F29, F06.0, F06.2 296.00 – 296.09, 296.40 – 296.79, 296.80, 296.89, 301.13; F31 312.80 – 312.81, 312.90 – 312.99, 313.81, 314.00 – 314.01, 314.90 – 314.99; F90, R46 All other codes .01 – 289.99, 320 – 997.99, V-codes, E-codes 999.97 – 999.99, 0.00; B-codes, D-codes, G-codes, I-codes, N-codes, O-codes, P-codes, 999.9997 – 999.9999, F99, R69, R99, Z03.89 | 14 | Anxiety disorders |
|  |  | 15 | Depressive disorders |
|  |  | 16 | Schizophrenic/other psychotic disorders |
|  |  | 17 | Bipolar disorders |
|  |  | 18 | Attention deficit/disruptive behavior disorders |
|  |  | 19 | Other mental health condition -9 Missing |

## Appendix C. Technical Notes

The TEDS report tables contain several variables created by combining or recoding original variables submitted by states. The following notes describe how these variables are created or recoded. Co-occurring use of drugs and alcohol:

- If primary substance use is 2 alcohol and secondary or tertiary substance use are valid drugs, then change primary substance use to 4 alcohol with secondary drug; otherwise, change primary substance use to 3 alcohol only;
- if primary substance use is valid drug and secondary or tertiary substance use is 2 alcohol, then change primary substance use to 2 drug with secondary alcohol;
- if primary substance use is 1 none or -9 missing/unknown/not collected/invalid, then change primary substance use to 5 no primary substance reported;
- otherwise, change primary substance use to 1 drug only. Recoding for primary substance use:
- If primary substance use is 2 alcohol and secondary or tertiary substance use are valid drugs, then change primary substance use to alcohol with secondary drug; otherwise, change primary substance use to alcohol only;
- if primary substance use is 6 non-prescription methadone or 7 other opiates and synthetics, then change primary substance use to other opiates;
- if primary substance use is 3 cocaine and primary route of administration is 2 smoking, then change primary substance use to crack;
- if primary substance use is 10 methamphetamines/speed or 11 other amphetamines, change primary substance use to methamphetamine/amphetamines;
- if primary substance use is 13 benzodiazepines or 14 other tranquilizers, change primary substance use to tranquilizers;
- if primary substance use is 15 barbiturates or 16 other sedatives or hypnotics, change primary substance use to sedatives;
- if primary substance use is 1 none, 12 other stimulants, 18 over-the-counter medications, or 19 other drugs, and -9 missing/unknown/not collected/invalid, then change primary substance use to other/none specified. The rest of the substances retain their original labels. Secondary and tertiary substance use follow the same recoding logic as above, except that secondary and tertiary substance use do not have an alcohol-only category. Marijuana involvement and referral source:
- If primary substance use is 2 alcohol and secondary drug and secondary or tertiary substance use is 4 marijuana/hashish, then change new variable to 1 both alcohol and marijuana;
- if primary substance use is 4 marijuana/hashish and secondary or tertiary substance use is 2 alcohol, then change new variable to 1 both alcohol and marijuana;

- otherwise, if primary substance use is 2 alcohol, change new variable to 2 primary alcohol, no marijuana;
- otherwise, if primary substance use is 4 marijuana/hashish, then change new variable to 3 primary marijuana, no alcohol;
- otherwise, if secondary or tertiary substance use is 4 marijuana/hashish, then change new variable to 4 marijuana not primary, no alcohol;
- otherwise, if primary, secondary and tertiary substance use are all not specified, then change new variable to 5 no substance reported;
- otherwise, change new variable to 6 other drugs and drug combinations. Create new format for variable referral source:
- Categories 1–6 are other referral source;
- category 7 is criminal justice referral. Flag variables represent any substance use among primary, secondary and tertiary substance use:
- If primary or secondary or tertiary substance use is 2 alcohol, then alcohol flag is 1;
- if primary or secondary or tertiary substance use is 5 heroin, then heroin flag is 1;
- if primary or secondary or tertiary substance use is 4 marijuana, then marijuana flag is 1;
- if primary or secondary or tertiary substance use is 3 cocaine, then cocaine flag is 1;
- if primary or secondary or tertiary substance use is crack new category, then crack flag is 1;
- if primary or secondary or tertiary substance use is 6 non-prescription methadone or 7 other opiates and synthetics, then opiate flag is 1;
- if primary or secondary or tertiary substance use is 8 PCP, then PCP flag is 1;
- if primary or secondary or tertiary substance use is 9 other hallucinogens, then hallucinogens flag is 1;
- if primary or secondary or tertiary substance use is 10 methamphetamines/speed or 11 other amphetamines, then amphetamine flag is 1;
- if primary or secondary or tertiary substance use is 13 benzodiazepines or 14 other tranquilizers, then tranquilizer flag is 1;
- if primary or secondary or tertiary substance use is 15 barbiturates or 16 other sedatives or hypnotics, then sedatives flag is 1;
- if primary or secondary or tertiary substance use is 17 inhalants, then inhalant flag is 1;
- if primary or secondary or tertiary substance use is 12 other stimulants, 18 over-the-counter medications, or 19 other drugs, then other flag is 1. Recoding service type:
- If service type is 6 ambulatory, intensive outpatient or 7 ambulatory, non-intensive outpatient and medication-assisted therapy is 1 yes, then new service type is medication- assisted opioid therapy outpatient;

- if service type is 1 24-hour hospital inpatient detoxification, 2 24-hour free-standing residential detoxification, or 8 ambulatory detoxification and medication-assisted therapy is 1 yes, then new service type is medication-assisted opioid therapy detoxification;
- if service type is in 3 hospital residential rehabilitation, 4 short-term residential rehabilitation, or 5 long-term residential rehabilitation and medication-assisted therapy is 1 yes, then new service type is medication-assisted opioid therapy residential. Coding number of substances: Create a new variable that calculates the number of substances (maximum of three) reported at admission for each client by summing the values within each observation for primary, secondary, and tertiary substances reported at admission.
