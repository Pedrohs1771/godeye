"""
GOĐEYE - Advanced Security Research Tool
Educational Proof of Concept for Web Security Analysis
Version: 2.0.0 | Author: Security Research

DISCLAIMER: This tool is for EDUCATIONAL PURPOSES only.
Use only on systems you own or have explicit permission to test.
Unauthorized access to computer systems is illegal.
"""

import json
import time
import asyncio
import re
import hashlib
from datetime import datetime
from typing import Dict, List, Optional, Any
from urllib.parse import urlparse
import traceback

# ============================================================================
# CONFIGURATION - Security Research Parameters
# ============================================================================

class ResearchConfig:
    """Configuration for security research and analysis"""
    
    # Rate limiting to prevent abuse
    REQUEST_DELAY = 1.0
    MAX_REQUESTS_PER_MINUTE = 30
    
    # Safe domains whitelist (for demo purposes)
    SAFE_DOMAINS = [
        'httpbin.org',
        'example.com',
        'localhost',
        'github.com',
        'stackoverflow.com'
    ]
    
    @staticmethod
    def get_browser_args() -> List[str]:
        """Browser arguments for security research"""
        return [
            '--disable-web-security',
            '--disable-features=IsolateOrigins,site-per-process',
            '--no-sandbox',
            '--disable-dev-shm-usage',
            '--disable-gpu',
            '--disable-notifications',
        ]

# ============================================================================
# HEADER ANALYZER - Security Headers Analysis
# ============================================================================

class HeaderAnalyzer:
    """Analyzes HTTP headers for security research"""
    
    def __init__(self):
        self.findings = []
        self.security_headers = {
            'Strict-Transport-Security': 'HSTS',
            'Content-Security-Policy': 'CSP',
            'X-Frame-Options': 'Clickjacking Protection',
            'X-Content-Type-Options': 'MIME Sniffing Protection',
            'Referrer-Policy': 'Referrer Policy'
        }
    
    async def analyze_headers(self, headers: Dict, url: str):
        """Analyze HTTP headers for security posture"""
        analysis = {
            'timestamp': datetime.now().isoformat(),
            'url': url[:100],
            'present_headers': [],
            'missing_headers': [],
            'recommendations': []
        }
        
        # Check security headers
        for header, name in self.security_headers.items():
            if header in headers:
                analysis['present_headers'].append(name)
            else:
                analysis['missing_headers'].append(name)
                analysis['recommendations'].append(f"Add {header} header")
        
        # Check for authentication headers (educational only)
        auth_headers = ['Authorization', 'Cookie', 'X-API-Key']
        for auth in auth_headers:
            if auth in headers:
                analysis['auth_found'] = True
                analysis['auth_type'] = auth
        
        self.findings.append(analysis)
        return analysis

# ============================================================================
# STREAM DETECTOR - Media Stream Analysis
# ============================================================================

class StreamDetector:
    """Detects and analyzes media streaming protocols"""
    
    STREAM_PATTERNS = {
        'HLS': r'\.m3u8|application/vnd\.apple\.mpegurl',
        'DASH': r'\.mpd|application/dash\+xml',
        'MPEG-DASH': r'dash|mpd',
        'HLS_SEGMENT': r'\.ts\b|video/mp2t',
    }
    
    def __init__(self):
        self.detected_streams = []
        
    async def detect(self, url: str, content_type: str) -> Optional[Dict]:
        """Detect streaming protocols in URLs and content types"""
        for stream_type, pattern in self.STREAM_PATTERNS.items():
            if re.search(pattern, url, re.IGNORECASE) or re.search(pattern, content_type, re.IGNORECASE):
                stream_info = {
                    'type': stream_type,
                    'url': url[:150],
                    'content_type': content_type,
                    'timestamp': datetime.now().isoformat()
                }
                self.detected_streams.append(stream_info)
                return stream_info
        return None

# ============================================================================
# API MAPPER - Endpoint Discovery
# ============================================================================

class APIMapper:
    """Discovers and maps API endpoints"""
    
    API_PATTERNS = [
        r'/api/',
        r'/v\d+/',
        r'/graphql',
        r'/rest/',
        r'\.json$',
    ]
    
    def __init__(self):
        self.endpoints = []
        self.stats = {'GET': 0, 'POST': 0, 'PUT': 0, 'DELETE': 0}
    
    async def analyze(self, url: str, method: str) -> Optional[Dict]:
        """Analyze if URL is an API endpoint"""
        is_api = any(re.search(pattern, url, re.IGNORECASE) for pattern in self.API_PATTERNS)
        
        if is_api:
            endpoint = {
                'url': url[:150],
                'method': method.upper(),
                'timestamp': datetime.now().isoformat()
            }
            self.endpoints.append(endpoint)
            self.stats[method.upper()] = self.stats.get(method.upper(), 0) + 1
            return endpoint
        return None

# ============================================================================
# COMMAND GENERATOR - Safe Replication Commands
# ============================================================================

class CommandGenerator:
    """Generates safe replication commands for educational purposes"""
    
    def __init__(self):
        self.commands = []
    
    def generate_curl(self, url: str, method: str = 'GET', headers: Dict = None) -> str:
        """Generate safe cURL command for educational analysis"""
        cmd_parts = ['curl']
        
        if method != 'GET':
            cmd_parts.append(f'-X {method}')
        
        # Add safe headers only (no sensitive data)
        if headers:
            safe_headers = ['User-Agent', 'Accept', 'Accept-Language']
            for key, value in headers.items():
                if key in safe_headers:
                    cmd_parts.append(f'-H "{key}: {value}"')
        
        cmd_parts.append(f'"{url}"')
        cmd_parts.append('--compressed')
        cmd_parts.append('--max-time 30')
        
        command = ' \\\n    '.join(cmd_parts)
        
        self.commands.append({
            'type': 'CURL',
            'url': url[:100],
            'command': command,
            'timestamp': datetime.now().isoformat()
        })
        
        return command
    
    def generate_mpv(self, url: str) -> str:
        """Generate safe MPV command for streaming analysis"""
        command = f'mpv "{url}" --no-cache --no-resume-playback --ytdl=no'
        self.commands.append({
            'type': 'MPV',
            'url': url[:100],
            'command': command,
            'timestamp': datetime.now().isoformat()
        })
        return command

# ============================================================================
# MAIN RESEARCH ENGINE
# ============================================================================

class GoDEyeResearch:
    """Main research engine for security analysis"""
    
    def __init__(self):
        self.header_analyzer = HeaderAnalyzer()
        self.stream_detector = StreamDetector()
        self.api_mapper = APIMapper()
        self.command_gen = CommandGenerator()
        
        self.stats = {
            'requests_analyzed': 0,
            'headers_analyzed': 0,
            'streams_detected': 0,
            'apis_discovered': 0
        }
        
        self.start_time = None
        self.is_active = False
    
    async def analyze_target(self, target_url: str, browser, page):
        """Main analysis routine"""
        self.is_active = True
        self.start_time = datetime.now()
        
        print(f"""
╔══════════════════════════════════════════════════════════════╗
║  GOĐEYE - Advanced Security Research Tool                    ║
║  Target: {target_url[:50]}...{' ' * (50 - len(target_url[:50]))}║
║  Started: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}                                    ║
╚══════════════════════════════════════════════════════════════╝
        """)
        
        # Setup request/response monitoring
        await self._setup_monitoring(page)
        
        # Navigate to target
        print(f"🌐 Navigating to target...")
        try:
            await page.goto(target_url, wait_until='networkidle', timeout=30000)
            print(f"✅ Page loaded successfully")
        except Exception as e:
            print(f"⚠️ Navigation timeout: {e}")
        
        print(f"\n📡 Monitoring for {30} seconds...")
        await asyncio.sleep(30)
        
        self.is_active = False
        self._print_report()
    
    async def _setup_monitoring(self, page):
        """Setup network monitoring"""
        
        async def on_request(request):
            if not self.is_active:
                return
            
            self.stats['requests_analyzed'] += 1
            
            # Analyze if this looks like an API
            url = request.url
            method = request.method
            
            endpoint = await self.api_mapper.analyze(url, method)
            if endpoint:
                self.stats['apis_discovered'] += 1
                print(f"🔗 API Discovered: {method} {url[:80]}...")
            
            # Generate safe cURL command for interesting requests
            if any(p in url.lower() for p in ['api', 'json', 'data']):
                cmd = self.command_gen.generate_curl(url, method, request.headers)
                print(f"📝 cURL command generated")
        
        async def on_response(response):
            if not self.is_active:
                return
            
            self.stats['headers_analyzed'] += 1
            
            # Analyze security headers
            headers = response.headers
            analysis = await self.header_analyzer.analyze_headers(headers, response.url)
            
            if analysis.get('missing_headers'):
                print(f"⚠️ Missing security headers: {', '.join(analysis['missing_headers'][:3])}")
            
            # Detect streaming content
            content_type = headers.get('content-type', '')
            stream = await self.stream_detector.detect(response.url, content_type)
            if stream:
                self.stats['streams_detected'] += 1
                print(f"🎬 Stream detected: {stream['type']}")
                
                # Generate MPV command
                cmd = self.command_gen.generate_mpv(response.url)
                print(f"🎥 MPV command generated")
        
        page.on('request', on_request)
        page.on('response', on_response)
    
    def _print_report(self):
        """Print research report"""
        duration = datetime.now() - self.start_time if self.start_time else 0
        
        print(f"""
╔══════════════════════════════════════════════════════════════╗
║  GOĐEYE - RESEARCH REPORT                                    ║
╠══════════════════════════════════════════════════════════════╣
║  Duration: {duration}                                                 ║
║  Requests Analyzed: {self.stats['requests_analyzed']}                                              ║
║  Headers Analyzed: {self.stats['headers_analyzed']}                                              ║
║  APIs Discovered: {self.stats['apis_discovered']}                                               ║
║  Streams Detected: {self.stats['streams_detected']}                                               ║
╠══════════════════════════════════════════════════════════════╣
║  📁 Output Files:                                             ║
║    • research_data.json - Full analysis data                 ║
║    • replication_commands.txt - Safe replication commands    ║
╚══════════════════════════════════════════════════════════════╝
        """)
    
    def save_data(self, filename: str = "research_data.json"):
        """Save research data"""
        data = {
            'metadata': {
                'tool': 'GOĐEYE',
                'version': '2.0.0',
                'timestamp': datetime.now().isoformat(),
                'duration': str(datetime.now() - self.start_time) if self.start_time else None
            },
            'findings': {
                'headers': self.header_analyzer.findings[-10:],
                'streams': self.stream_detector.detected_streams[-10:],
                'apis': self.api_mapper.endpoints[-20:],
                'commands': self.command_gen.commands[-10:]
            },
            'statistics': self.stats
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        # Save commands to separate file
        with open("replication_commands.txt", 'w', encoding='utf-8') as f:
            f.write("# GOĐEYE - Safe Replication Commands\n")
            f.write(f"# Generated: {datetime.now()}\n")
            f.write("#" * 60 + "\n\n")
            
            for cmd in self.command_gen.commands:
                f.write(f"# {cmd['type']} - {cmd['url']}\n")
                f.write(f"{cmd['command']}\n\n")
        
        print(f"💾 Data saved to {filename} and replication_commands.txt")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

async def main():
    """Main entry point"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║  ░██████╗░█████╗░██████╗░███████╗██╗░░░██╗███████╗         ║
    ║  ██╔════╝██╔══██╗██╔══██╗██╔════╝╚██╗░██╔╝██╔════╝         ║
    ║  ██║░░░░░██║░░██║██║░░██║█████╗░░░╚████╔╝░█████╗░░         ║
    ║  ██║░░░░░██║░░██║██║░░██║██╔══╝░░░░╚██╔╝░░██╔══╝░░         ║
    ║  ╚██████╗╚█████╔╝██████╔╝███████╗░░░██║░░░███████╗         ║
    ║  ░╚═════╝░╚════╝░╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝         ║
    ║                                                              ║
    ║  Advanced Security Research Tool v2.0                       ║
    ║  Educational Purpose Only                                   ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    print("""
    ⚠️  DISCLAIMER:
    This tool is for EDUCATIONAL and AUTHORIZED SECURITY RESEARCH only.
    Using this tool against systems you don't own or have permission to test
    is ILLEGAL. The author assumes no liability for misuse.
    
    By continuing, you confirm you will only use this tool for:
    • Learning about web security
    • Testing your own applications
    • Authorized penetration testing
    """)
    
    confirm = input("\nDo you accept these terms? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("Exiting...")
        return
    
    try:
        from playwright.async_api import async_playwright
        
        async with async_playwright() as p:
            print("\n🔧 Initializing browser...")
            browser = await p.chromium.launch(
                headless=False,
                args=ResearchConfig.get_browser_args()
            )
            
            context = await browser.new_context(
                viewport={'width': 1280, 'height': 720},
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            )
            
            page = await context.new_page()
            
            print("\n🎯 Enter target URL for analysis:")
            print("   (Examples: https://httpbin.org, https://example.com)")
            target = input("URL: ").strip()
            
            if not target.startswith('http'):
                target = 'https://' + target
            
            # Run analysis
            research = GoDEyeResearch()
            await research.analyze_target(target, browser, page)
            
            # Save results
            research.save_data()
            
            await browser.close()
            
            print("\n✅ Analysis complete!")
            print("📁 Check research_data.json and replication_commands.txt")
            
    except ImportError:
        print("\n❌ Playwright not installed.")
        print("   Run: pip install playwright && playwright install")
    except KeyboardInterrupt:
        print("\n\n🛑 Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    import warnings
    warnings.filterwarnings('ignore')
    asyncio.run(main())