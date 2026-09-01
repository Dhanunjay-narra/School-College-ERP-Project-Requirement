from writer_util import write_f

def generate_mobile():
    print("[MOBILE] Generating Flutter / Dart Mobile Client Applications...")

    write_f("mobile/pubspec.yaml", '''name: school_college_erp_mobile
description: Enterprise Unified Mobile Application for Students, Parents, and Faculty
version: 1.0.0+1
environment:
  sdk: ">=3.0.0 <4.0.0"

dependencies:
  flutter:
    sdk: flutter
  http: ^1.2.0
  flutter_bloc: ^8.1.3
  google_fonts: ^6.1.0
  shared_preferences: ^2.2.2
  qr_code_scanner: ^1.0.1
  flutter_local_notifications: ^17.0.0
  geolocator: ^11.0.0

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^3.0.0

flutter:
  uses-material-design: true
''')

    write_f("mobile/lib/main.dart", '''import 'package:flutter/material.dart';
import 'screens/student_dashboard.dart';

void main() {
  runApp(const ERPMobileApp());
}

class ERPMobileApp extends StatelessWidget {
  const ERPMobileApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Apex ERP Mobile',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: const Color(0xFF0284C7)),
        useMaterial3: true,
      ),
      home: const StudentDashboardScreen(),
    );
  }
}
''')

    write_f("mobile/lib/screens/student_dashboard.dart", '''import 'package:flutter/material.dart';

class StudentDashboardScreen extends StatelessWidget {
  const StudentDashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Student Portal — Aarav Patel'),
        backgroundColor: const Color(0xFF0284C7),
        foregroundColor: Colors.white,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                gradient: const LinearGradient(
                  colors: [Color(0xFF0369A1), Color(0xFF1E3A8A)],
                ),
                borderRadius: BorderRadius.circular(16),
              ),
              child: const Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('Semester 4 • Computer Science', style: TextStyle(color: Colors.white70, fontSize: 12)),
                  SizedBox(height: 4),
                  Text('Roll No: 24CSE042', style: TextStyle(color: Colors.white, fontSize: 18, fontWeight: FontWeight.bold)),
                  SizedBox(height: 12),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    children: [
                      Text('CGPA: 8.85', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                      Text('Attendance: 94.2%', style: TextStyle(color: Color(0xFF6EE7B7), fontWeight: FontWeight.bold)),
                    ],
                  )
                ],
              ),
            ),
            const SizedBox(height: 20),
            const Text('Today\'s Classes', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
            const SizedBox(height: 10),
            _buildClassCard('CS401: Distributed Systems', '09:00 - 10:00 AM', 'Room 101 • Dr. David Smith'),
            _buildClassCard('CS402: Artificial Intelligence', '10:00 - 11:00 AM', 'Room 101 • Prof. Ananya Iyer'),
          ],
        ),
      ),
    );
  }

  Widget _buildClassCard(String title, String time, String location) {
    return Card(
      elevation: 1,
      margin: const EdgeInsets.only(bottom: 12),
      child: ListTile(
        leading: const CircleAvatar(
          backgroundColor: Color(0xFFE0F2FE),
          child: Icon(Icons.school, color: Color(0xFF0284C7)),
        ),
        title: Text(title, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14)),
        subtitle: Text(location, style: const TextStyle(fontSize: 12)),
        trailing: Text(time, style: const TextStyle(fontSize: 12, fontWeight: FontWeight.w600, color: Color(0xFF0284C7))),
      ),
    );
  }
}
''')

    write_f("mobile/lib/screens/parent_dashboard.dart", '''import 'package:flutter/material.dart';

class ParentDashboardScreen extends StatelessWidget {
  const ParentDashboardScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Parent Portal')),
      body: const Center(child: Text('Ward Overview & Fee Notifications')),
    );
  }
}
''')

    write_f("mobile/lib/screens/transport_tracker.dart", '''import 'package:flutter/material.dart';

class TransportTrackerScreen extends StatelessWidget {
  const TransportTrackerScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Live Bus GPS Tracking')),
      body: const Center(child: Text('Bus Route #01 — ETA 12 mins')),
    );
  }
}
''')

    print("[MOBILE] Flutter / Dart Mobile client code generated.")

if __name__ == '__main__':
    generate_mobile()
