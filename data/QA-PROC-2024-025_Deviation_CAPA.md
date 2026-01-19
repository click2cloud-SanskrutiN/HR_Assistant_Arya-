================================================================================
PT BIO FARMA - QUALITY ASSURANCE DEPARTMENT
================================================================================

Document ID: QA-PROC-2024-025
Title: DEVIATION MANAGEMENT AND CAPA PROCESS
Version: 4.0
Effective Date: January 20, 2024
Department: Quality Assurance
Classification: GMP Critical

================================================================================
APPROVAL SIGNATURES
================================================================================
Prepared by: Fitri Handayani, QA Specialist              Date: 10-Jan-2024
Reviewed by: Budi Santoso, Head of Quality Assurance     Date: 15-Jan-2024
Approved by: Dr. Ratna Dewi, VP Quality & Compliance     Date: 20-Jan-2024

================================================================================
1. PURPOSE
================================================================================
This procedure establishes the systematic process for identifying, 
documenting, investigating, and resolving deviations from established 
procedures, specifications, and GMP requirements. It also defines the 
process for implementing Corrective and Preventive Actions (CAPA) to 
prevent recurrence.

================================================================================
2. SCOPE
================================================================================
This procedure applies to ALL deviations occurring in:
- Manufacturing operations
- Quality control testing
- Quality assurance activities
- Engineering and maintenance
- Material management
- Environmental monitoring
- Cleaning and sanitization

Applicable to:
- Planned deviations (approved protocol deviations)
- Unplanned deviations (incidents, errors, out-of-specification results)
- Critical deviations (patient safety impact)
- Major deviations (GMP compliance impact)
- Minor deviations (limited impact)

================================================================================
3. DEFINITIONS
================================================================================

Deviation: Any departure from approved procedures, specifications, or 
           regulatory requirements.

Critical Deviation: Deviation with potential impact on product quality, 
                   patient safety, or data integrity. Requires immediate 
                   action and senior management notification.
                   Examples: Contamination event, equipment malfunction 
                   affecting sterility, OOS result for critical parameter

Major Deviation: Deviation affecting GMP compliance or quality but with 
                no immediate patient safety risk. Requires investigation 
                and CAPA.
                Examples: Procedure not followed, documentation error, 
                environmental monitoring excursion

Minor Deviation: Deviation with negligible impact on product quality.
                May not require formal investigation.
                Examples: Typographical error in record, delayed signature 
                (within same day)

Root Cause: The fundamental reason(s) a deviation occurred, which if 
           eliminated, would prevent recurrence.

CAPA: Corrective Action (fix the problem) and Preventive Action (prevent 
      recurrence or occurrence of potential problems).

Effectiveness Check: Verification that CAPA has successfully resolved the 
                    issue and prevented recurrence.

================================================================================
4. RESPONSIBILITIES
================================================================================

4.1 Any Employee (Initiator)
    - Identify and report deviations immediately
    - Complete Deviation Report form
    - Provide factual information during investigation
    - Implement immediate containment actions

4.2 Department Supervisor
    - Review and classify deviation severity
    - Assign investigation owner
    - Approve investigation plan
    - Monitor investigation timeline
    - Approve corrective actions

4.3 Quality Assurance
    - Review all deviations for GMP impact
    - Determine batch disposition (release/reject)
    - Approve CAPA plans
    - Conduct effectiveness checks
    - Trend analysis of deviations
    - Report to senior management

4.4 Senior Management
    - Review critical deviations within 24 hours
    - Approve resource allocation for CAPA
    - Review deviation trends quarterly

================================================================================
5. PROCEDURE
================================================================================

5.1 DEVIATION IDENTIFICATION & REPORTING

5.1.1 Recognition
    Deviations must be identified when:
    - Procedure not followed as written
    - Equipment malfunction or failure
    - Out-of-specification (OOS) test result
    - Environmental monitoring alert/action limit exceeded
    - Material or product quality issue
    - Documentation error or omission
    - Training requirement not met
    - Contamination or cross-contamination event

5.1.2 Immediate Actions (Within 1 hour)
    
    Step 1: STOP affected operation if continuing poses risk
            - Secure materials/product (quarantine)
            - Preserve evidence (samples, photos, equipment settings)
            - Do not discard anything related to deviation
    
    Step 2: Notify supervisor IMMEDIATELY
            - Verbal notification (in-person or phone)
            - Provide brief description
            - For CRITICAL deviations: Also notify QA Manager immediately
    
    Step 3: Implement containment action
            - Prevent further impact
            - Isolate affected batch/materials
            - Label clearly: "ON HOLD - DEVIATION #_____"
            - Secure area if contamination involved

5.1.3 Deviation Report Initiation (Same day)
    
    Step 1: Access Deviation Management System
            - Login to QMS software (DocuTrack v8.2)
            - Select "New Deviation Report"
            - System assigns unique Deviation Number (DEV-2024-XXXX)
    
    Step 2: Complete Deviation Report Form (Section 1: Identification)
            
            Required Information:
            
            ☐ Date/Time deviation discovered: ___/___/____ at ____:____
            ☐ Location: Building/Room/Equipment: _______________
            ☐ Product/Batch affected: _______________
            ☐ Batch status at time of deviation: _______________
               (In-process / Finished / Released / Shipped)
            ☐ Initiator name: _______________
            ☐ Department: _______________
            
            Deviation Description (Be specific and factual):
            - What happened? (Observable facts only, no opinions)
            - When was it discovered?
            - What procedure/specification was violated?
            - What is the normal/expected condition?
            
            Example GOOD description:
            "During aseptic filling operation on 2024-01-15 at 14:30, 
            operator noticed differential pressure between Grade A and 
            Grade B areas decreased from 15 Pa to 7 Pa. Per SOP-MFG-
            2024-018, minimum required is 12 Pa. Filling was stopped 
            immediately. Approximately 450 vials had been filled at time 
            of discovery."
            
            Example POOR description:
            "Pressure problem during filling. Might have contamination."
            [Too vague, lacks facts, includes speculation]
    
    Step 3: Attach supporting documents
            ☐ Batch production record pages (if applicable)
            ☐ Equipment logs/printouts
            ☐ Environmental monitoring data
            ☐ Photographs (if relevant)
            ☐ Material certificates/labels
    
    Step 4: Submit to Supervisor for review
            - Click "Submit for Review"
            - Supervisor receives automatic email notification
            - Timeline starts: Supervisor must review within 24 hours

5.2 DEVIATION CLASSIFICATION

5.2.1 Supervisor Review (Within 24 hours of report submission)
    
    Step 1: Verify deviation description accuracy
            - Interview initiator if needed
            - Visit site if required
            - Add any additional information
    
    Step 2: Classify deviation severity
            Use decision tree below:

            ┌─────────────────────────────────────────────────┐
            │ Does deviation impact product sterility,        │
            │ potency, or patient safety?                     │
            └────────┬────────────────────────┬────────────────┘
                     │ YES                    │ NO
                     ▼                        ▼
              ┌──────────────┐         ┌──────────────────┐
              │   CRITICAL   │         │ Does deviation   │
              │  DEVIATION   │         │ affect GMP       │
              └──────────────┘         │ compliance?      │
                                       └────┬──────────┬──┘
                                            │ YES      │ NO
                                            ▼          ▼
                                      ┌────────┐  ┌──────┐
                                      │ MAJOR  │  │MINOR │
                                      └────────┘  └──────┘
    
    Classification Examples:
    
    CRITICAL:
    - Sterility test failure
    - Contamination in sterile product
    - Equipment failure affecting product quality
    - OOS result for potency or safety parameter
    - Cross-contamination between products
    - Data integrity breach
    
    MAJOR:
    - Environmental monitoring action limit exceeded
    - Procedure not followed (no quality impact confirmed)
    - Equipment preventive maintenance overdue
    - OOS result for non-critical parameter
    - Documentation error requiring record recreation
    - Training expired at time of operation
    
    MINOR:
    - Late signature on document (same shift)
    - Typographical error (no data affected)
    - Environmental monitoring alert limit exceeded (not action)
    - Minor spill (contained, cleaned, documented)
    
    Step 3: Assign investigation owner
            - Typically: Process owner or subject matter expert
            - For critical: Senior staff member
            - Enter name in system: _______________
    
    Step 4: Set investigation timeline
            - Critical: Investigation complete within 5 working days
            - Major: Investigation complete within 10 working days
            - Minor: Investigation complete within 15 working days
    
    Step 5: Notify Quality Assurance
            - System automatically sends email to QA
            - QA reviews within 24 hours
            - QA determines batch disposition:
              □ Release approved (after investigation if minor)
              □ Hold (pending investigation completion)
              □ Reject (quality impact confirmed)

5.3 INVESTIGATION

5.3.1 Investigation Planning (Within 2 days of assignment)
    
    Step 1: Form investigation team (if needed for critical/major)
            Team may include:
            - Investigation owner (lead)
            - Process operator(s) involved
            - Supervisor
            - QA representative
            - Engineering (if equipment-related)
            - Subject matter expert
    
    Step 2: Hold initial meeting
            - Review deviation details
            - Develop investigation plan
            - Assign specific tasks
            - Set internal milestones
    
    Step 3: Document investigation plan in system
            Planned activities:
            ☐ Interview personnel
            ☐ Review procedures/training records
            ☐ Inspect equipment
            ☐ Review historical data/trends
            ☐ Test/sample analysis
            ☐ Consult with expert
            ☐ Literature review
            ☐ Other: _______________

5.3.2 Investigation Execution
    
    Step 1: Gather factual information
            
            Personnel Interviews:
            - Who was involved?
            - What were they doing?
            - What did they observe?
            - When did it happen?
            - Document verbatim quotes
            
            Document Review:
            - Batch production records
            - Equipment logs
            - Training records for personnel involved
            - Previous similar deviations
            - Procedure versions (verify correct version used)
            
            Physical Evidence:
            - Equipment inspection
            - Materials examination
            - Environmental conditions
            - Process parameters at time of event
    
    Step 2: Reconstruct timeline
            Create chronological sequence:
            - What was supposed to happen?
            - What actually happened?
            - When did deviation occur?
            - When was it discovered?
            - What happened between occurrence and discovery?
    
    Step 3: Analyze data
            - Compare actual vs expected
            - Look for patterns or trends
            - Check historical performance
            - Statistical analysis if relevant

5.3.3 Root Cause Analysis
    
    Use structured approach (select based on complexity):
    
    Method 1: 5 Whys (for simple deviations)
    Ask "Why?" iteratively until root cause identified
    
    Example:
    Deviation: Tank overfilled
    Why? - Operator didn't stop pump at level sensor
    Why? - Level sensor alarm didn't activate
    Why? - Sensor was not calibrated on schedule
    Why? - Calibration schedule wasn't updated after new equipment
    Why? - Change control didn't include PM schedule update
    ROOT CAUSE: Change control process inadequate
    
    Method 2: Fishbone Diagram (for complex deviations)
    Analyze 6M categories: Man, Machine, Method, Material, 
    Measurement, Mother Nature (Environment)
    
    Method 3: Fault Tree Analysis (for critical deviations)
    Work backwards from event using logic gates
    
    Step 1: Identify all potential causes
            Brainstorm with team
            Consider:
            - Human error (knowledge, skill, fatigue, communication)
            - Equipment (design, malfunction, calibration, age)
            - Procedure (clarity, accuracy, accessibility)
            - Material (quality, storage, handling)
            - Environment (temperature, contamination, layout)
            - Training (adequate, documented, understood)
    
    Step 2: Verify root cause(s)
            Test each potential root cause:
            - If eliminated, would deviation be prevented?
            - Is there evidence supporting this cause?
            - Is it a symptom or actual root cause?
            
            Common mistake: Stopping at "human error"
            Always ask: WHY did human error occur?
            - Procedure unclear?
            - Training inadequate?
            - Equipment design confusing?
            - Fatigue/distraction factors?
    
    Step 3: Document root cause in system
            - State clearly and specifically
            - Provide supporting evidence
            - Explain verification method

5.3.4 Impact Assessment
    
    Step 1: Assess product impact
            Questions to address:
            - Does deviation affect product quality attributes?
            - Which batches are potentially affected?
            - Is product safe for use?
            - Does product meet specifications?
            - Additional testing needed?
    
    Step 2: Assess GMP compliance impact
            - What requirement was violated?
            - Regulatory reporting required?
              (Critical deviation: Report to regulatory authority 
              within 3 days)
            - Documentation adequate?
    
    Step 3: Determine batch disposition
            QA makes final decision:
            
            RELEASE:
            - Investigation complete
            - Root cause identified
            - No quality impact confirmed
            - Batch meets all specifications
            - CAPA implemented or planned
            
            REJECT:
            - Quality impact confirmed
            - Specification not met
            - Cannot ensure product quality/safety
            
            ADDITIONAL INVESTIGATION:
            - Conduct additional testing
            - Extend investigation
            - Keep on hold status

5.3.5 Investigation Report
    
    Complete Deviation Report (Section 2: Investigation)
    
    Required Content:
    
    ☐ Investigation Summary
      - Activities performed
      - Personnel interviewed
      - Documents reviewed
      - Tests conducted
    
    ☐ Timeline Reconstruction
      - Chronological sequence of events
    
    ☐ Root Cause Analysis
      - Method used (5 Whys, Fishbone, etc.)
      - Root cause statement
      - Supporting evidence
    
    ☐ Impact Assessment
      - Product quality impact
      - GMP compliance impact
      - Affected batches identified
    
    ☐ Batch Disposition Recommendation
      - Release, Reject, or Further Investigation
      - Justification
    
    ☐ CAPA Plan (see Section 5.4)
    
    ☐ Attachments
      - Interview notes
      - Photos
      - Test results
      - Analysis diagrams
    
    Step: Submit for management review
          - Supervisor review and approve
          - QA review and approve
          - For Critical: Senior Management review required

5.4 CORRECTIVE AND PREVENTIVE ACTION (CAPA)

5.4.1 CAPA Development
    
    Step 1: Identify corrective actions (fix the problem)
            
            Must directly address root cause
            
            Examples:
            Root Cause: Procedure unclear
            Corrective Action: Revise procedure with step-by-step photos
            
            Root Cause: Training inadequate
            Corrective Action: Develop hands-on training module with 
                              competency assessment
            
            Root Cause: Equipment lacks fail-safe
            Corrective Action: Install automated shut-off valve
            
            Avoid weak CAPAs:
            ✗ "Retrain operator" (too vague)
            ✓ "Conduct classroom + hands-on training on proper sampling 
               technique with written competency test (≥80% pass)"
            
            ✗ "Be more careful" (not actionable)
            ✓ "Implement double-check system with supervisor verification 
               before critical step"
    
    Step 2: Identify preventive actions (prevent recurrence)
            
            Consider:
            - Can this happen elsewhere?
            - Similar processes/equipment?
            - Need system-wide change?
            
            Examples:
            - If procedure unclear for one product, review all similar 
              procedures
            - If equipment issue, check all units of same model
            - If training gap, assess training program adequacy
    
    Step 3: Risk assessment of no action
            If CAPA not implemented, what's the risk?
            - Likelihood of recurrence: Low / Medium / High
            - Severity of impact: Low / Medium / High
            - Is CAPA justified by risk?
    
    Step 4: Define CAPA details
            For EACH corrective/preventive action, specify:
            
            ☐ Action Description (specific, measurable)
            ☐ Action Owner (name, title)
            ☐ Target Completion Date (realistic timeline)
            ☐ Resources Required (budget, equipment, personnel)
            ☐ Success Criteria (how will we know it's complete?)
            ☐ Effectiveness Check Method (how will we verify it works?)
            ☐ Effectiveness Check Date (typically 30-90 days after 
              implementation)

5.4.2 CAPA Approval
    
    Step 1: Supervisor approval
            - Verify CAPA addresses root cause
            - Confirm resources available
            - Approve action owners and timelines
    
    Step 2: QA approval
            - Verify adequacy of CAPA
            - Confirm GMP compliance restored
            - Approve effectiveness check plan
    
    Step 3: For Critical deviations: Senior Management approval
            - Review resource requirements
            - Approve capital expenditures if needed
            - Final authorization to proceed

5.4.3 CAPA Implementation
    
    Step 1: Execute corrective actions
            - Action owner completes assigned task
            - Document completion in system
            - Upload evidence:
              □ Revised procedure (if applicable)
              □ Training records (if applicable)
              □ Work order completion (if maintenance)
              □ Purchase order (if new equipment)
              □ Photos of implemented change
    
    Step 2: Update status in system
            - Mark action as "Complete"
            - Enter actual completion date
            - Add completion notes
    
    Step 3: QA verification
            - Review evidence of completion
            - Verify action implemented as described
            - Approve as complete or return for correction

5.4.4 Effectiveness Check
    
    Conducted 30-90 days after CAPA implementation
    
    Step 1: Define effectiveness criteria (during CAPA planning)
            
            Examples:
            - If CAPA = revised procedure
              Effectiveness = No similar deviations occur for 3 months
            
            - If CAPA = training
              Effectiveness = Competency assessment scores ≥90% and 
                            no related errors for 60 days
            
            - If CAPA = equipment modification
              Effectiveness = Equipment performs within specifications 
                            for 90 days with no failures
    
    Step 2: Collect effectiveness data
            - Review deviation log (similar deviations?)
            - Interview personnel (change sustainable?)
            - Check performance metrics
            - Audit records (procedure followed correctly?)
    
    Step 3: Determine effectiveness
            ✓ EFFECTIVE: Success criteria met, no recurrence
            ✗ INEFFECTIVE: Issue recurred or success criteria not met
            
            If ineffective:
            - Re-open investigation
            - Develop revised CAPA
            - May need deeper root cause analysis
    
    Step 4: Document effectiveness check
            - Complete Effectiveness Check section in system
            - Provide evidence (data, metrics, records)
            - QA reviews and approves
            - Close deviation officially if effective

5.5 CLOSURE

5.5.1 Final Review Checklist
    
    Before closing deviation, verify:
    ☐ Investigation complete and documented
    ☐ Root cause identified with evidence
    ☐ Impact assessment complete
    ☐ Batch disposition determined
    ☐ CAPA developed and approved
    ☐ CAPA implemented with evidence
    ☐ Effectiveness check completed (if required)
    ☐ All sections of report complete
    ☐ All approvals obtained
    ☐ Regulatory reporting completed (if required)

5.5.2 Final Approvals
    
    Approval Sequence:
    1. Investigation Owner signs
    2. Department Supervisor approves
    3. QA Manager approves
    4. For Critical: VP Quality approves
    
    System automatically sends notification at each approval stage

5.5.3 Record Archival
    
    - System archives deviation with all attachments
    - Deviation number remains in searchable database
    - Records retained per retention policy (minimum 10 years)

5.6 TREND ANALYSIS

5.6.1 Quarterly Deviation Review (QA Responsibility)
    
    Step 1: Generate deviation metrics
            - Total deviations (by severity)
            - Deviations by department
            - Deviations by type (procedure, equipment, OOS, etc.)
            - Average investigation time
            - CAPA effectiveness rate
    
    Step 2: Identify trends
            - Increasing deviation rate?
            - Repeat deviations (CAPA ineffective)?
            - Common root causes?
            - Departments needing support?
    
    Step 3: Report to Management Review Meeting
            - Present trends and metrics
            - Recommend system-wide CAPAs if needed
            - Propose resources/support
    
    Step 4: Implement system-level improvements
            - Training program enhancements
            - Procedure standardization
            - Equipment upgrades
            - Organizational changes

================================================================================
6. TIMELINES SUMMARY
================================================================================

Action                              Timeline
─────────────────────────────────────────────────────────────────────────
Deviation identification            Immediate (same day)
Supervisor classification           Within 24 hours
QA review                           Within 24 hours of classification
Investigation completion:
  - Critical deviation              Within 5 working days
  - Major deviation                 Within 10 working days
  - Minor deviation                 Within 15 working days
CAPA implementation                 As per approved plan (30-90 days typical)
Effectiveness check                 30-90 days post-implementation
Regulatory reporting (Critical)     Within 3 days

Extension requests must be approved by QA Manager with documented justification.

================================================================================
7. REGULATORY REPORTING
================================================================================

7.1 Critical Deviations Requiring Reporting
    Report to regulatory authority (BPOM) within 3 days if:
    - Product sterility compromised
    - Contamination in released product
    - Product recall potential
    - Serious quality defect
    - Data integrity issue affecting released batches

7.2 Reporting Process
    - QA prepares Field Alert Report
    - Medical Safety evaluates patient risk
    - VP Quality approves report
    - Regulatory Affairs submits to BPOM
    - Follow-up investigation report submitted within 30 days

================================================================================
8. METRICS & KPIs
================================================================================

Tracked Monthly:
- Total deviations (target trend: decreasing)
- % Critical deviations (target: <5% of total)
- % Investigations completed on time (target: >90%)
- Average investigation duration (target: <7 days for major)
- % CAPA completed on time (target: >85%)
- % CAPA deemed effective (target: >95%)
- Repeat deviations (target: <3%)

================================================================================
9. TRAINING REQUIREMENTS
================================================================================

All employees must complete:
- Initial training on this procedure during onboarding
- Annual refresher training
- Additional training if procedure revised

Role-specific training:
- Supervisors: Root cause analysis methods (8 hours)
- QA staff: Advanced investigation techniques (16 hours)
- Investigators: CAPA development workshop (4 hours)

Training documented in Learning Management System (LMS)

================================================================================
10. RELATED DOCUMENTS
================================================================================
SOP-QA-2024-018: Out-of-Specification Investigation
SOP-QA-2024-022: Change Control Management
SOP-QA-2024-030: Document Management System
SOP-TRAIN-2023-001: Training and Competency Assessment
FORM-DEV-001: Deviation Report Template
FORM-CAPA-002: CAPA Plan Template

================================================================================
REVISION HISTORY
================================================================================
Version  Date        Description                                 Author
4.0      20-Jan-2024 Major revision - added effectiveness check F. Handayani
                     requirements, updated timelines
3.5      10-May-2023 Added regulatory reporting section          B. Santoso
3.0      15-Aug-2022 Implemented electronic deviation system     F. Handayani
2.8      20-Jan-2022 Updated CAPA approval process               R. Dewi

================================================================================
END OF DOCUMENT
================================================================================